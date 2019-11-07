from socket import *
import time
import threading
import sys
from _thread import start_new_thread

#PORT_NUMBER = 7851
PORT_NUMBER = 8591
HOST_NAME = '69.61.103.44'
RTT = []
BUFFER_SIZE = 4096
ADDRESS = (HOST_NAME,PORT_NUMBER)
UDPPacketNumber = 1;

udpSocket = socket(AF_INET,SOCK_DGRAM)
#This thread will handle sending msgs, and embedding the time in each message before sending
class Thread_SentFrom(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name


    def run(self):
        global flag
        numberMessagesSent=0
        msgToSendToClient = "This is for the UDP Server:"
        global udpSocket
        #udpSocket = socket(AF_INET,SOCK_DGRAM)
        while numberMessagesSent < 5:
            numberMessagesSent = numberMessagesSent+1
            sentTime = time.time()
            msgToSendToClient = "This is for the UDP Server:"+str(sentTime)
            udpSocket.sendto(msgToSendToClient.encode('utf_8'),ADDRESS)





#thread that will handle receiving msgs and calculating the RTT and all other stats
class Thread_ReceivedFrom(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        numberMessagesRcvd=0
        msgRcvd = udpSocket.recvfrom(BUFFER_SIZE)
        #test = msgRcvd.splice(":")
        print("This is test:",msgRcvd)
        #Note for future:
        #Figure out how the msg will be returned from Prof's Server, then we know how to parse it
        # to get the numbers from each msg, Then we print out the related stats that we can
        #get from those numbers.
        #We have no guarantee that the messages we send will be received back in order, we can send
        #msg 1 and receive it last, so we can not rely on recording the time we send it and check
        #the time.time() on the client to calculate the RTT
        #we have to embed time sent in  each msg, and then parse it from each received msg and
        #calculate that with the clients current time.time()

        #at least thats my thinking

a = Thread_SentFrom("SendingThread_A")
b = Thread_ReceivedFrom("ReceivingThread_B")

a.start()
b.start()

a.join()
b.join()
#Both threads will be finished by this point, .join tells the python program to wait for them
# before going on

udpSocket.close()