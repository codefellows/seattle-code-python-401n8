from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
# new
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Take the url query string and create a dictionary of parameters
        url = self.path
        url_components = parse.urlsplit(url)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)  # /?word=something

        # We can do stuff!
        print(dictionary)
        dictionary_api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{dictionary.get('word')}"
        response = requests.get(dictionary_api_url)
        data = response.json()
        # print(data)
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        print(definition)

        # forming the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f"The definition of {dictionary.get('word')} is: {definition}".encode())


if __name__ == '__main__':
    server_address = ('localhost', 8000)  # use any available port
    httpd = HTTPServer(server_address, handler)  # httpd is a commonly used abbreviation for "HTTP Daemon"
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
