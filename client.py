import time
from socket import *

totalNumberOfPings = 0
lostPackets = 0
totalRTTTime = 0
eachRTTTime = 0
percentLoss = 0
#Send ping 10 times
for pings in range(1000):
    totalNumberOfPings = totalNumberOfPings + 1
    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    #Set a timeout value of 1 second
    clientSocket.settimeout(2.0)
    #Ping to server
    message = 'This is the message'
    #Losseless Server
    #serveraddress = ("69.61.103.44", 7851)
    #Lossy Server
    serveraddress = ("69.61.103.44", 8591)

    #Start Time
    startTime = time.time()
    #Send message
    clientSocket.sendto(message.encode('utf_8'), serveraddress)

    try:
        data, server = clientSocket.recvfrom(1024)
        endTime = time.time()
        eachRTTTime = endTime - startTime
        totalRTTTime = totalRTTTime + eachRTTTime
        #print (data)
        #print ("Each rtt time", eachRTTTime)
        #print("The total time of RTT is ", totalRTTTime)

    #If data is not received back from server, print it has timed out
    except timeout:
        lostPackets = lostPackets + 1
        print ('REQUEST TIMED OUT')

percentLoss = ((lostPackets / totalNumberOfPings) * 100)
print("The percent loss is ", percentLoss)
print("The total number of packets sent is ", totalNumberOfPings)
print("The total time of RTT is ", totalRTTTime)
print("The packet average RTT is ", totalRTTTime/totalNumberOfPings)
print("The total lost packets are " , lostPackets)