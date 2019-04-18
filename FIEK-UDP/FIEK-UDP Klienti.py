import socket
import sys

#serverAddressPort  = ("localhost", 12000)

serverName = "localhost"
port = 12000

var = input('Emri i serverit eshte: ' + serverName + ' dhe porti eshte ' + str(
    port) + ' , A dëshironi te i ndryshoni? (PO/JO) - > ')
if var.upper() == "PO":
    serverName = input('Emri i serverit: -> ')
    port = int(input('Numri i portit: -> '))

serverAddressPort = (serverName, port)

print('+-----------------------------------------------+---------------------------------------------------+')
print('|            Sintaksa e komandave               |           Lista e parametrave Opcioni jane:       |')
print('+-----------------------------------------------+---------------------------------------------------+')
print('|                  IPADRESA                     |                 KilowattToHorsepower              |')
print('|                NUMRIIPORTIT                   |                 HorsepowerToKilowatt              |')
print('|              EMRIIKOMPJUTERIT                 |                   DegreesToRadians                |')
print('|                    KOHA                       |                   RadiansToDegrees                |')
print('|                    LOJA                       |                    GallonsToLiters                |')
print('|           PRINTIMI {Hapesire} text            |                    LitersToGallons                |')
print('|       BASHKETINGELLORE {Hapesire} text        |                                                   |')
print('|KONVERTIMI {Hapesire} Opcioni {Hapesire} number|                                                   |')
print('|         FIBONACCI {Hapesire} number           |                                                   |')
print('|       DECIMALTOBINARY {Hapesire} number       |                                                   |')
print('|    DECIMALTOHEKSADECIMAL {Hapesire} number    |                                                   |')
print('+-----------------------------------------------+---------------------------------------------------+')
print('\n\n')


UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    var = input(
        '\nJu lutem shenoni kerkesen: ' + '\n(IPADRESA, NUMRIIPORTIT, EMRIIKOMPJUTERIT, KOHA, LOJA, PRINTIMI, BASHKETINGELLORE, KONVERTIMI, FIBONACCI, DECIMALTOBINARY, DECIMALTOHEKSADECIMAL):'
        + '\n -> ')

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

