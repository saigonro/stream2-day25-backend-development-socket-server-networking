#!/usr/bin/env python3
import socket

IP = '127.0.0.1'
PORT = 1246
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048

serversocket = socket.socket()
serversocket.bind((IP, PORT))
serversocket.listen(MAXIMUM_QUEUE_SIZE)
print('Hi there! I am listening now')

while True:
    (clientsocket, client_ip_and_port) = serversocket.accept()
    response = "Hi there at ip address %s and port %s\nPlease enter empty line to quit\n"
    clientsocket.send(response.encode())
    while True:
        client_message = clientsocket.recv(BUFFER_SIZE).decode()
        if not client_message.rstrip:
            break
        response = "you sent %s" % client_message
        clientsocket.send(response.encode())
    clientsocket.send("You choose to quit, bye, see you later".encode())
    clientsocket.close()