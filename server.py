from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        mimetype = None
        if (self.path == '/'):
            f = open('index.html', 'rb')
            mimetype = 'text/html'
        if (self.path == '/d3.js'):
            f = open('d3.js', 'rb')
            mimetype = 'application/javascript'
        if (self.path == '/data/td1.csv'):
            f = open('data/td1.csv', 'rb')
            mimetype = 'text/csv'

        if mimetype is not None:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Invalid path')
        return

if __name__ == '__main__':
    sv = HTTPServer(("", 8080), Handler)
    sv.serve_forever()
