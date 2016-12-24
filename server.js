const http = require('http')
const fs   = require('fs')
const port = process.env.PORT || 1337;
const indexPayload = fs.readFileSync('index.html', 'utf8')
const coverPaylaod = fs.readFileSync('cover.css', 'utf8')

console.log('Starting web server on port ' + port)

http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200)
    res.write(indexPayload)
  }
  else if (req.url === '/cover.css') {
    res.writeHead(200)
    res.write(coverPaylaod)
  }
  else {
    res.writeHead(404)
    res.write('File not found')
  }
  res.end()
}).listen(port);

