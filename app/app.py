from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo
import requests


app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# TO-DO - change from hard coded to get values from env variables
MONGO_HOST = 'localhost'
MONGO_USER = 'root'
MONGO_PASS = '1234'
MONGO_PORT = '27018'
MONGO_DB = 'admin'

USER_COLLECTION = 'users'
SDK_COLLECTION = 'sdk'

VAST_EP = 'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast'

mongo_client = pymongo.MongoClient('mongodb://' +
                                   MONGO_USER +
                                   ':' + MONGO_PASS +
                                   '@' + MONGO_HOST +
                                   ':' + MONGO_PORT + '/')
db = mongo_client[MONGO_DB]

@app.route('/')
def hello():
    res = {}
    return jsonify(res)

@app.route('/GetAd', methods=['GET'])
def get_ad():
    # Get Params from the request
    # The rest variables from the assignment will not be in use (session_id, platform, country)
    data = request.get_json()
    sdk_version = request.args.get('sdk_version')
    user_name = request.args.get('user_name')

    # If both params exist in request increment the action amount
    if sdk_version is not None and user_name is not None:
        user_cnt(user_name,'requests')
        sdk_cnt(sdk_version, 'requests')

    # Return Vast ad response
    return get_vast()

@app.route('/Impression')
def set_impression():
    # Get Params from the request
    # The rest variables from the assignment will not be in use (session_id, platform, country)
    data = request.get_json()
    sdk_version = request.args.get('sdk_version')
    user_name = request.args.get('user_name')

    # If both params exist in request increment the action amount
    if sdk_version is not None and user_name is not None:
        user_cnt(user_name,'impressions')
        sdk_cnt(sdk_version, 'impressions')

    return ('', 204)

@app.route('/GetStats')
def get_stats():
    # Get Params from the request
    filter_type = request.args.get('filter_type')

    # Run rate calculation quesry on DB
    result = get_calculated_rate(filter_type)
    if result is not None:
        return jsonify(result)

    return jsonify({})



def user_cnt(id,action):
    try:
        collection = db[USER_COLLECTION]
        collection.update({'user_id': id},
                          {'$inc': {'impressions': 1 if action == 'impressions' else 0,
                                    'requests': 1 if action == 'requests' else 0}},
                          upsert=True)
    except:
        print("Error occured while updating DB")

def sdk_cnt(id, action):
    try:
        collection = db[SDK_COLLECTION]
        collection.update({'sdk': id},
                          {'$inc': {'impressions': 1 if action == 'impressions' else 0,
                                    'requests': 1 if action == 'requests' else 0}},
                          upsert=True)
    except:
        print("Error occured while updating DB")

def get_vast():
    try:
        response = requests.get(VAST_EP)
        if response.status_code == 200:
            body = response.content
            return body.decode('utf-8')
    except:
        print("Error occured while requesting vast")
        return None

def get_calculated_rate(type):
    try:
        collection = db[type]
        result = collection.aggregate(get_rate_query())
        return list(result)
    except:
        print("Error occured while running calculation")
        return None

def get_rate_query():
    return [{
            '$addFields': {
                'rate': {
                    # handle zero derived case & calculate rate
                    '$cond': [{ '$eq': ["$impressions", 0]}, 0, {"$divide": ['$requests', '$impressions']}]
                },
                # Remove irrelevant fields
                'impressions' : '$$REMOVE',
                'requests' : '$$REMOVE',
                '_id' : '$$REMOVE'
            }
        }]

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
