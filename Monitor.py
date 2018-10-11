#!usr/bin/python3.6
# Basicly monitor is attached on a traffic light and keeps on monitoring the 
# status of traffic accidences, sending out denm messages (notifications for vehicles)
# and receving 

from Event import Event

import time
import serial
import sys
import os
import re

Event_flag = 0
MAX_LOOP_NUM = 100000

def waitForCmdRsp():
    pass

def waitForCmdOKRsp():
    maxloopNum = 0
    while True:
        line = ser.readline()
        maxloopNum = maxloopNum + 1
        
        try:
            print("Rsponse : %s"%line.decode('utf-8'))
        except:
            pass
            
        if ( re.search(b'successfully',line)):
            break
        elif(maxloopNum > MAX_LOOP_NUM):
            sys.exit(0)

# Send commands to Unex
def sendAT_Cmd(serInstance,atCmdStr,waitforSuccess):
    print("Sending: %s"%atCmdStr)
    serInstance.write(atCmdStr.encode('utf-8'))
    #or define b'string',bytes should be used not str
    if(waitforSuccess == 1):
        waitForCmdOKRsp()
    else:
        waitForCmdRsp()

#Test = Event(1,6,1000,2000)
#Test.print_status()

ser = serial.Serial("/dev/ttyUSB0",115200,timeout=30)

while(1):
    while(Event_flag!=0):
        pass
    sendAT_Cmd(ser,'camReceiving 10000\r',1)







