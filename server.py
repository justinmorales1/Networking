from socket import *
import sys
from time import ctime

PORT_NUMBER = 10000
LOCAL_HOST = 'localhost'
BUFFER_SIZE = 4096
serverAddress = (LOCAL_HOST,PORT_NUMBER)

#Create the UDP socket
udpSocket = socket(AF_INET,SOCK_DGRAM)

#Bind it to server address
udpSocket.bind(serverAddress)

while True:
    print("--------- Waiting for the  message ---------")
    data, address = udpSocket.recvfrom(BUFFER_SIZE)

    if data is None:
        break

    print("The data that was received is ", data.decode('utf-8'))
    newData = data.upper()
    print(newData.decode('utf-8'))
    if data:
        sentData = udpSocket.sendto(newData, address)

udpSocket.close()
    
    