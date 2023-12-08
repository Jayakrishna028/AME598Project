var express = require('express');
var MS = require('mongoskin');
var bodyParse = require('body-parser');
var app = express();
var hostname = process.env.HOSTNAME || 'localhost';
// var hostname = 192.168.0.130;

var distanceFront = 0;
var distanceRight = 0;
var distanceLeft = 0;
var reqTime = 0;

app.use(express.static(__dirname));
var port = 8080;
var db = MS.db("mongodb://localhost:27017/sensorData");


console.log("The server is running at http://localhost:8080");

//Just a basic redirect to index.html
app.get("/" ,function(req, res){ 
    res.redirect("index.html");
});

app.get("/getSensorData", function(req, res){
    app.redirect("")
});

// Processing the data from the car and add it to the database
app.get("/sendSensorData", function(req, res) {
    distanceFront = req.query.distanceFront;
    distanceRight = req.query.distanceRight;
    distanceLeft = req.query.distanceLeft;
    reqTime = new Date().getTime();

    // Create a single data point object with three vectors
    var dataObj = {
        vectors: [
            { x: 0, y: distanceFront, z: 0 },
            { x: distanceRight, y: 0, z: 0 },
            { x: -distanceLeft, y: 0, z: 0 }
        ],
        reqTime: reqTime
    };

    console.log(dataObj);

    // Insert the data point into the "dataPoints" collection
    db.collection("dataPoints").insert(dataObj, function(err, result) {
        if (err) {
            console.error("Error adding data point:", err);
            res.status(500).send('Error');
        } else {
            console.log("Added data point");
            res.send('ok');
        }
    });
});

app.get("/getValue", function (req, res) {
    //res.writeHead(200, {'Content-Type': 'text/plain'});
    res.send(reqTime.toString() + " " + distanceFront + " " + distanceRight + " " + distanceLeft + "\r");
  });

  app.get("/getLatestThree", function(req, res) {
    db.collection("dataPoints").find().sort({ reqTime: -1 }).limit(3).toArray(function(err, results) {
        if (err) {
            res.status(500).send("Error fetching data");
        } else {
            res.json(results);
        }
    });
});


app.listen(port);