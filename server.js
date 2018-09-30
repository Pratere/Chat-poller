var http = require('http');
var url = require('url');

var server = http.createServer(function(req, res) {
var result = "PLACEHOLDER"

res.writeHead(200, {"Content-Type": "text/plain"});

res.write(result+" is the greatest response");
res.end();
});
server.listen(8080);
