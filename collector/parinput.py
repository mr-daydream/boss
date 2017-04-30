#!/usr/bin/python
import socket
import time
import serial

ser = serial.Serial('/dev/ttyS0')

CARBON_SERVER = '104.131.45.105'
CARBON_PORT = 2003
array = []
while True:
        line = ser.readline()
        if len(line) == 51:
            mydict = dict(item.split(':') for item in line.split())
            tempmsg = "center1.bed%s.temp %s %i\n" % (mydict['N'][-1:], mydict['T'], int(time.time())) 
            print 'sending message:\n%s' % tempmsg
            sock = socket.socket()
            sock.connect((CARBON_SERVER, CARBON_PORT))
            sock.sendall(tempmsg)
            sock.close()
            bendmsg = "center1.bed%s.bend %s %i\n" % (mydict['N'][-1:], mydict['B'], int(time.time())) 
            print 'sending message:\n%s' % bendmsg
            sock = socket.socket()
            sock.connect((CARBON_SERVER, CARBON_PORT))
            sock.sendall(bendmsg)
            sock.close()
            time.sleep(1)
ser.close()
