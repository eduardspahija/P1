import socket
import sys

def Main():

    serverName = '192.168.0.21'
    port = 12000

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

    var = input('Emri i serverit eshte: ' + serverName + ' dhe porti eshte ' + str(port) + ' , A dëshironi te i ndryshoni? (PO/JO) - > ')
    if var.upper() == "PO":
        serverName = input('Emri i serverit: -> ')
        port = int(input('Numri i portit: -> '))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverName, port))

    while True:

        var = input('Ju lutem shenoni kerkesen: -> ')

        s.send(var.encode())
        r = s.recv(1024).decode()

        print('Te dhenat e pranuara nga serveri', r)

        answer = input('A dëshironi të vazhdoni? (PO/JO) -> ')
        if answer.upper() == 'PO':
            continue
        else:
             break
    s.close()
	
if __name__ == '__main__':
    Main()

