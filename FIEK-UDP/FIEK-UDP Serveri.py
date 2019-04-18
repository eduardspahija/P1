from socket import *
import datetime
import random
import string
import os

def IPADRESA(ClientIpAddr):
    return "IP Adresa e klientit eshte: " + ClientIpAddr

def NUMRIIPORTIT(ClientPortNo):
    return "Klienti eshte duke perdorur portin: " + str(ClientPortNo)

def BASHKETINGELLORE(tekst):

    type(tekst)
    vowels = 0
    consonants = 0
    others = 0

    for i in tekst:
        if (i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'  or i == 'Y'
        or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'  or i == 'y'
        ):

            vowels = vowels + 1
        elif  (i not in string.ascii_letters):

            others = others + 1
        else:
             consonants = consonants + 1

    return "Teksti i pranuar permban " + str(consonants) + " bashkentingellore"

def PRINTIMI(tekst):

    return tekst

def EMRIIKOMPJUTERIT():
    try:
      host = os.environ['COMPUTERNAME']
      return "Emri I klientit eshte " + host
    except:
      return "Emri i klientit nuk dihet "

def KOHA():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S %p")

def LOJA():
    resp = ""
    for x in range (7):
      resp = resp + str(random.randint(1, 50))
      if x < 6:
        resp = resp + ", "
    return resp

def KONVERTIMI(llojiKonvertimit, vlera):

    if llojiKonvertimit.upper() == "KilowattToHorsepower".upper():
      kilowatt = vlera
      horsepower = round(float(kilowatt) * 1.34102,2)
      return str(kilowatt) + " kilowatt = " + str(horsepower) + " horsepower"
    elif llojiKonvertimit.upper() == "HorsepowerToKilowatt".upper():
      horsepower = vlera
      kilowatt = round(float(horsepower) / 1.34102,2)
      return str(horsepower) + " horsepower = " + str(kilowatt) + " kilowatt"
    elif llojiKonvertimit.upper() == "DegreesToRadians".upper():
      degrees = vlera
      radians = round(float(degrees) * 0.0174533,2)
      return str(degrees) + " degrees = " + str(radians) + " radians"
    elif llojiKonvertimit.upper() == "RadiansToDegrees".upper():
      radians = vlera
      degrees = round(float(radians) / 0.0174533,2)
      return str(radians) + " radians = " + str(degrees) + " degrees"
    elif llojiKonvertimit.upper() == "GallonsToLiters".upper():
      gallon = vlera
      liter = round(float(gallon) * 3.7854,2)
      return str(gallon) + ' gallon(US) = ' + str(liter) + ' liter'
    elif llojiKonvertimit.upper() == "LitersToGallons".upper():
      liter = vlera
      gallon = round(float(liter) / 3.7854,2)
      return str(liter) + ' liter = ' + str(gallon) + ' gallon(US)'
    else:
      return "Nuk ekziston kjo kerkese"

def FIBONACCI(n):
    if n<0:
        print("Numri duhet te jete me i madh se zero")
    elif n == 1:  
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return FIBONACCI(n-1) + FIBONACCI(n-2)

def DECIMALTOBINARY(n):
    x = n
    k = []
    while (n > 0):
        a = int(float(n % 2))
        k.append(a)
        n = (n - a) / 2
    k.append(0)
    string = ""
    for j in k[::-1]:
        string = string + str(j)
    return string

def DECIMALTOHEKSADECIMAL(n):
        x = (n % 16)
        c = ""
        if (x < 10):
            c = x
        if (x == 10):
            c = "A"
        if (x == 11):
            c = "B"
        if (x == 12):
            c = "C"
        if (x == 13):
            c = "D"
        if (x == 14):
            c = "E"
        if (x == 15):
            c = "F"

        if (n - x != 0):
            return DECIMALTOHEKSADECIMAL(n / 16) + str(c)
        else:
            return str(c)


def ERROR():
    return "Kerkesa jo valide"


serverName = 'localhost'
serverPort = 12000

UDPServerSocket = socket(AF_INET, SOCK_DGRAM)
UDPServerSocket.bind((serverName, serverPort))

print('Serveri eshte startuar ne localhost ne portin ' + str(serverPort) + '.')

print('Serveri eshte i gatshem te pranoj kerkesa.')

while True:

    bytesAddressPair = UDPServerSocket.recvfrom(1024)

    ClientRequest = bytesAddressPair[0].decode().upper()

    address = bytesAddressPair[1]
    clientIPAddr = address[0]
    clientPort = address[1]

    print("Client IP Address:{}".format(address))

    if ClientRequest == "NUMRIIPORTIT":
        response = NUMRIIPORTIT(clientPort)
    elif ClientRequest == "IPADRESA":
        response = IPADRESA(clientIPAddr)
    elif ClientRequest.startswith("BASHKETINGELLORE"):
        arg = ClientRequest.split(" ", 1)
        teksti= arg[1]
        response = BASHKETINGELLORE(teksti)
    elif ClientRequest.startswith("PRINTIMI"):
        arg = ClientRequest.split(" ", 1)
        teksti= arg[1]
        fjala = (PRINTIMI(teksti)).lower()
        response = fjala.capitalize()
    elif ClientRequest == "EMRIIKOMPJUTERIT":
        response = EMRIIKOMPJUTERIT()
    elif ClientRequest == "KOHA":
        response = KOHA ()
    elif ClientRequest == "LOJA":
        response = LOJA()
    elif ClientRequest.startswith("KONVERTIMI"):
        args = ClientRequest.split(" ", 2)
        llojiKonvertimit = args[1]
        vlera = int(args[2])
        response = KONVERTIMI(llojiKonvertimit, vlera)
    elif ClientRequest.startswith("FIBONACCI"):
        arg = ClientRequest.split(" ", 1)
        numri = int(arg[1])
        response = str(FIBONACCI(numri))
    elif ClientRequest.startswith("DECIMALTOBINARY"):
        arg = ClientRequest.split(" ", 1)
        numri = int(arg[1])
        response = DECIMALTOBINARY(numri)
    elif ClientRequest.startswith("DECIMALTOHEKSADECIMAL"):
        arg = ClientRequest.split(" ", 1)
        numri = int(arg[1])
        response = DECIMALTOHEKSADECIMAL(numri)

    else:
        response = "Kerkesa eshte jovalide"

    response = str.encode(response)

    UDPServerSocket.sendto(response, address)
