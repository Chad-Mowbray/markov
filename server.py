import socket
import datetime
import json
from markov import MarkovGenerator

class Request:
    def __init__(self, request_text):
        self.parse_request(request_text.recv(4096).decode('utf-8').split('\r\n'))
    
    def parse_request(self, decoded_request_text):
        self.parsed_request = {"uri": decoded_request_text[0].split(" ")[1]}

def build_html_response(text_body):
    html_body = f'<html><head><title>An Example Page</title></head><body>{text_body}</body></html>'
    return f"HTTP/1.1 200 OK\r\nContent-Type:text/html\r\nContent-Length:{len(html_body)}\r\nAccess-Control-Allow-Origin:*\r\n\r\n{html_body}"

def build_json_response():
    mg = MarkovGenerator()
    mg.run()
    json_body = json.dumps({"random_text": mg.generate_text(20)})
    return f"HTTP/1.1 200 OK\r\nContent-Type:application/json\r\nContent-Length:{len(json_body)}\r\nAccess-Control-Allow-Origin:*\r\n\r\n{json_body}"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # so you don't have to change ports when restarting
server.bind(('0.0.0.0', 9292))


while True:
    server.listen()
    print("waiting for a request on localhost:9292")
    client_connection, _client_address = server.accept()
    client_request = Request(client_connection)
    if client_request.parsed_request['uri'] == '/':
        client_connection.send(build_html_response('Hello World').encode())
    elif client_request.parsed_request['uri'] == '/random_poe':
        client_connection.send(build_json_response().encode())
