var express = require('express');
var app = express();
var bodyParse = require('body-parser');
var hostname = process.env.HOSTNAME || 'localhost';
// var hostname = 192.168.0.130;

app.use(express.static(__dirname));
var port = 8080;

console.log("The server is running at http://localhost:8080");

app.get("/" ,function(req, res){ 
    res.redirect("index.html");
});

app.get("/getSensorData", function(req, res){
    app.redirect("")
});

app.get("/sendSensorData", function(req, res){
    distanceFront = req.query.distanceFront;
    distanceRight = req.query.distanceRight;
    distanceLeft = req.query.distanceLeft;
    req.query.time = new Date().getTime();
    console.log(distanceFront, distanceRight, distanceLeft);

    res.send('ok');
});

app.listen(port);