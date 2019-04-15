import socket
import sys

serverName = '192.168.0.21'
port = 12000
var = raw_input('Ju lutem shenoni kerkesen: -> ')
while var.lower().strip() != "quit":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverName, port))
    s.sendall(var.encode())
    r = s.recv(1024)
    print('Te dhenat e pranuara nga serveri', r)
    var = raw_input('Ju lutem shenoni kerkesen: -> ')
    s.close()

