# Sayollo Home Assigment

<b>Design:</b>
<p>
The application written in Python 3.9 with Flask which help me to create the web server </p>
<b>DB choice: </b>
I choise MongoDB as the DB for this application for few reasons:
<ul>
<li>Mongodb is more easy to scale in comperason to relational DB</li>
<li>Mongo DB allow us to use an atomic increment operation to count the amount of requests/impressions. Thats mean that we can update the counter only by one operation without check if the id exist -> get current vale -> increase by one</li>
</ul>

<b>Libraries:</b>
<ul>
<li>Flask - For the web server</li>
<li>Flask CORS - To make our API available for cross domain requests</li>
<li>pymongo - MongoDB client</li>
<li>requests - To make the external request</li>
</ul>

<b>Global Variables:</b>
</br></br>
The variables defined hardcoded in the script in constants.</br>
Its better to get the variables from Environment Variables by the os library that will initate during the docker image deploy. </br>
If we will plan to use K8S we can also set them in secret files then we will not expose sensetive information in our Repository

<b>How to run:</b>

By Docker:
Running the following code will create 2 containers of MongoDB and Flask application

``` docker
cd <Project Path>
docker-compose up
```

After the image will build and container will be ready we can send http request to our server in the following url:
``` 
http://localhost:5000
```

<p>To test our application we can run the folloing request to our server:</p>
</br>

New Request:
```curl
curl -X GET "http://127.0.0.1:5000/GetAd?sdk_version=1.1.0&user_name=Niso" 
Response:
<VAST xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="2.0"><Ad><InLine><Error><![CDATA[]]></Error><Creatives><Creative><Linear><Duration>00:00:06</Duration><MediaFiles><MediaFile><![CDATA[https://sayollo.nyc3.digitaloceanspaces.com/Covid4.webm]]></MediaFile></MediaFiles><TrackingEvents /></Linear></Creative></Creatives></InLine></Ad></VAST>
```

New Impression:
```curl
curl -X GET "http://127.0.0.1:5000/Impression?sdk_version=1.1.0&user_name=Niso" 
Response:
No Content. 204 status code
```

Statistic:
```curl
curl -X GET "http://127.0.0.1:5000/GetStats?filter_type=users"
curl -X GET "http://127.0.0.1:5000/GetStats?filter_type=sdk" 
Response:
[{"rate":0,"user_id":"dana"},{"rate":2.0,"user_id":"yossi"},{"rate":0.6666666666666666,"user_id":"benni"},{"rate":2.0,"user_id":"danny"}]
```

</br></br>
<h4>Thanks for the opportunity!</h4>


