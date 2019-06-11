from http.server import HTTPServer, BaseHTTPRequestHandler

import pandas as pd

df = pd.DataFrame([[23, 44], [238, 234], [264, 472]])

def parseURL(s):
    groups = s.split('/')
    meth = groups[0]
    tags = groups[1].split('&')
    fmt = None
    times, _, fmt = groups[2].rpartition('.')
    times = times.split('_')
    return [meth, tags, times, fmt]


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        mimetype = None
        if (self.path == '/'):
            f = open('index.html', 'rb')
            mimetype = 'text/html'
        elif (self.path == '/parallel') or (self.path == '/p'):
            f = open('parallel.html', 'rb')
            mimetype = 'text/html'
        elif (self.path == '/lineplot') or (self.path == '/l'):
            f = open('lineplot.html', 'rb')
            mimetype = 'text/html'
        elif (self.path == '/parallel_style.css'):
            f = open('parallel_style.css', 'rb')
            mimetype = 'text/css'
        elif (self.path == '/js/d3.js'):
            f = open('js/d3.js', 'rb')
            mimetype = 'application/javascript'
        elif (self.path == '/datafiles/td1.csv'):
            f = open('data/td1.csv', 'rb')
            mimetype = 'text/csv'
        elif (self.path == '/data/iris.csv'):
            f = open('data/iris.csv', 'rb')
            mimetype = 'text/csv'
        elif (self.path[:5] == '/dat/'):
            print(self.path[5:])

            self.send_response(200)
            self.send_header('Content-type', 'text/csv')
            self.end_headers()
            self.wfile.write(df.to_csv().encode('utf-8'))
            return

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
