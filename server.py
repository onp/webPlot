from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        mimetype = None
        if (self.path == '/'):
            f = open('index.html', 'rb')
            mimetype = 'text/html'
        if (self.path == '/parallel') or (self.path == '/p'):
            f = open('parallel.html', 'rb')
            mimetype = 'text/html'
        if (self.path == '/parallel_style.css'):
            f = open('parallel_style.css', 'rb')
            mimetype = 'text/css'
        if (self.path == '/d3/d3.js'):
            f = open('d3/d3.js', 'rb')
            mimetype = 'application/javascript'
        if (self.path == '/data/td1.csv'):
            f = open('data/td1.csv', 'rb')
            mimetype = 'text/csv'
        if (self.path == '/data/iris.csv'):
            f = open('data/iris.csv', 'rb')
            mimetype = 'text/csv'

        if mimetype is not None:
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Invalid path')
        return


if __name__ == '__main__':
    port = 8080
    sv = HTTPServer(("", port), Handler)
    print('Serving on {}'.format(port))
    sv.serve_forever()
