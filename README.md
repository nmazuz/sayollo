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

How to run:
