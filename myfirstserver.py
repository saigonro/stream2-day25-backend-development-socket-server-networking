#!/usr/bin/env python3
import socket

IP = '0.0.0.0'
PORT = 8080
MAXIMUM_QUEUE_SIZE = 5
BUFFER_SIZE = 2048

def respond(clientsocket, client_ip_and_port):
    request = clientsocket.recv(BUFFER_SIZE).decode()
    request_lines = request.splitlines()
    request_itself = request_lines[0]
    other_request_lines = request_lines[1:-1]
    response_headers = "HTTP/1.1 200 OK\n\n"
    response_body_heading = "<h1>You ask for:</h1>\n"
    response = response_headers + response_body_heading + request_itself
    clientsocket.send(response.encode())

def serverloop():
    serversocket = socket.socket()
    serversocket.bind((IP, PORT))
    serversocket.listen(MAXIMUM_QUEUE_SIZE)
    
    while True:
        (clientsocket, client_ip_and_port) = serversocket.accept()
        respond(clientsocket, client_ip_and_port)
        clientsocket.close()

print('server launched on %s:%s' % (IP, PORT))
serverloop()