var express = require('express');
var app = express();
var bodyParse = require('body-parser');
var hostname = process.env.HOSTNAME || 'localhost';

app.use(express.static(__dirname));
var port = 8080;

console.log("The server is running at http://localhost:8080");

app.get("/" ,function(req, res){ 
    res.redirect("index.html");
});

app.get("/getSensorData", function(req, res){
    app.redirect("")
})
app.listen(port);