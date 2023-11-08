from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Take the url string and create a dictionary of the parameters
        url = self.path
        print("self.path is:", url)
        url_components = parse.urlsplit(url)  # returns a SplitResult() object
        print("url_components is:", url_components)  # we're only interested in the query
        query_string_list = parse.parse_qsl(url_components.query)  # a list of tuples, representing query parameters
        print("query_string_list is:", query_string_list)

        # dictionary = {i[0]: i[1] for i in query_string_list}
        dictionary = dict(query_string_list)
        print("the dictionary is:", dictionary)

        # We can do stuff! `dictionary` has our query parameters in a convenient data structure
        name = dictionary.get("name")
        age = dictionary.get("age")

        if name and age:
            message = f"Aloha {name}! you are {age} years old."
        else:
            message = f"Aloha stranger!"

        # forming the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())


if __name__ == '__main__':
    server_address = ('localhost', 8000)  # use any available port
    httpd = HTTPServer(server_address, handler)  # httpd is a commonly used abbreviation for "HTTP Daemon"
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
