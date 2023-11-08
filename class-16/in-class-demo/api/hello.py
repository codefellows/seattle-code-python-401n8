# The route name is: /api/hello
from http.server import BaseHTTPRequestHandler, HTTPServer


# use this class name with lowercase h!
class handler(BaseHTTPRequestHandler):
    # use this exact method name!
    def do_GET(self):  # this is the /api/hello GET endpoint
        message = "Hello World!"
        self.send_response(200)  # HTTP code
        self.send_header('Content-type', 'text/plain')  # defines the content type
        self.end_headers()  # add a blank line
        self.wfile.write(message.encode())


if __name__ == '__main__':
    server_address = ('localhost', 8000)  # use any available port
    httpd = HTTPServer(server_address, handler)  # httpd is a commonly used abbreviation for "HTTP Daemon"
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
