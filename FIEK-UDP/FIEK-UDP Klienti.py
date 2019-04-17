import socket
import sys

serverAddressPort  = ("192.168.0.21", 12000)

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    var = input('Ju lutem shenoni kerkesen: -> ')

    var = str.encode(var)

    UDPClientSocket.sendto(var, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(1024)

    msg = "Te dhenat e pranuara nga serveri: {}".format(msgFromServer[0].decode())

    print(msg)

    pergjegja = input('A dëshironi të vazhdoni? (PO/JO) -> ')

    if pergjegja.upper() == 'PO':
        continue
    elif pergjegja.upper() == 'JO':
        break
    else:
        print("Pergjigjia juaj nuk eshte valide!")
        break

UDPClientSocket.close()

