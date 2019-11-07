# from socket import *
# import time
# import threading
#
# PORT_NUMBER = 8581
# # HOST_NAME = 'localhost'
# RTT = []
# #PORT_NUMBER = 7851
# HOST_NAME = '69.61.103.44'
# BUFFER_SIZE = 4096
# ADDRESS = (HOST_NAME,PORT_NUMBER)
# UDPPacketNumber = 1;
# TotalRoundTripArray = []
# count = 0
# totalRTTTime = 0
# numberOfLostPackets = 0;
#
#
# #Setup my socket
# udpSocket = socket(AF_INET,SOCK_DGRAM)
#
# msgToSendToClient = "This is for the UDP Server"
#
# while count < 1:
#     #Start time for the RTT
#     startTime = time.time()
#
#     #Send the data to server
#     udpSocket.sendto(msgToSendToClient.encode('utf_8'),ADDRESS)
#
#     print("----- Waiting for response -----")
#     #The returned data from the server
#     recvData = udpSocket.recvfrom(BUFFER_SIZE)
#
#     #The RTT end time
#     endTime = time.time()
#
#     #The RTT total time
#     totalTime = str(endTime - startTime)
#     #Get a total RTT for all the messages sent
#     totalRTTTime += endTime - startTime
#
#     TotalRoundTripArray.append(totalTime)
#
#     #Print the total time
#     print("The Round Trip Time is " + totalTime)
#
#     #Print the returned data.
#     if recvData is not None:
#        print("The returned data is ----", recvData)
#     #Count for the number of messages sent
#     count += 1
#
#
# # numberOfLostPackets = str((10-len(TotalRoundTripArray))*10)
# print("The total number of packets sent is ", count)
# print("The number of packets that came back ", len(TotalRoundTripArray))
# print("The number of packets that were lost", count - len(TotalRoundTripArray))
# print("The total time of RTT is ", totalRTTTime)
# print("The packet average RTT is ", totalRTTTime/count)
#
# print(TotalRoundTripArray)
# #Close socket
# udpSocket.close()

import time
from socket import *

pings = 1
lostPackets = 0
#Send ping 10 times
while pings < 1000:

    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #Set a timeout value of 1 second
    clientSocket.settimeout(1)

    #Ping to server
    message = 'Sending data to server'
    #Non Losseless Server
    #addr = ("69.61.103.44", 7851)
    #Lossy Server
    serveraddress = ("69.61.103.44", 8591)

    #Send ping
    startTime = time.time()
    clientSocket.sendto(message.encode('utf_8'), serveraddress)

    #If data is received back from server, print
    try:
        data, server = clientSocket.recvfrom(1024)
        endTime = time.time()
        totalTime = endTime - startTime
        print (data)
        print (pings)
        print (totalTime)

    #If data is not received back from server, print it has timed out
    except timeout:
        lostPackets = lostPackets + 1
        print ('REQUEST TIMED OUT')

    pings = pings + 1

print("The total lost packets are " , lostPackets)