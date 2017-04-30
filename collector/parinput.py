#!/usr/bin/python
import socket
import time

CARBON_SERVER = '104.131.45.105'
CARBON_PORT = 2003
array = []
with open('sampleoutput.txt') as f:
        content = f.read().splitlines()
        for line in content:
                mydict = dict(item.split(':') for item in line.split())
                tempmsg = "center1.bed%s.temp %s %i\n" % (mydict['N'], mydict['T'], int(time.time())) 
                print 'sending message:\n%s' % tempmsg
                sock = socket.socket()
                sock.connect((CARBON_SERVER, CARBON_PORT))
                sock.sendall(tempmsg)
                sock.close()
                bendmsg = "center1.bed%s.bend %s %i\n" % (mydict['N'], mydict['B'], int(time.time())) 
                print 'sending message:\n%s' % bendmsg
                sock = socket.socket()
                sock.connect((CARBON_SERVER, CARBON_PORT))
                sock.sendall(bendmsg)
                sock.close()
                time.sleep(1)
