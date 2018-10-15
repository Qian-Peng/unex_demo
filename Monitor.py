#!usr/bin/python3.6
# Basicly monitor is attached on a traffic light or RSU and keeps on monitoring the 
# status of traffic, sending out denm messages (notifications for vehicles) if events happen

from Event import Event

import time
import serial
import sys
import os
import re

# Simulate event trigger
global Event_flag
Event_flag = 1

# Can be used to limit show up messages
MAX_LOOP_NUM = 100000

# A list to store vehicle ids in a circle
global vehicles_id
vehicles_id = []

# The content of simulated event according to DENM definition
demo_event = Event(1,6,2,0)

# Record vehicle ids
def calcualteVe(line):
    ve_id = int(line[19:])
    global vehicles_id
    if(vehicles_id.count(ve_id)==0):
        vehicles_id.append(ve_id)

# Waiting for Unex responses after sending out denm msgs,
# could be extended with more functions
def waitForDenmSRsp():
    maxloopNum = 0
    while True:
        line = ser.readline().decode()
        maxloopNum = maxloopNum + 1        
        try:
            print("Rsponse : "+line)
        except:
            pass
        if ( re.search(r'successfully',line)):
            break
        elif(maxloopNum > MAX_LOOP_NUM):
            sys.exit(0)


# Waiting for Unex responses after sending out Cam_Rec msgs,
# if cam is received, it will be processed
def waitForCamRRsp():
    maxloopNum = 0
    while True:
        line = ser.readline().decode()
        maxloopNum = maxloopNum + 1
        
        try:
            print("Rsponse : "+line)
        except:
            pass
        if(re.search(r'message_id',line)):
            calcualteVe(line) 
        if ( re.search(r'successfully',line)):
            break
        elif(maxloopNum > MAX_LOOP_NUM):
            sys.exit(0)

# Send commands to Unex
def sendAT_Cmd(serInstance,atCmdStr,waitforSuccess):
    print("Sending: %s"%atCmdStr)
    serInstance.write(atCmdStr.encode('utf-8'))
    #or define b'string',bytes should be used not str
    if(waitforSuccess == 1):
        waitForCamRRsp()
    else:
        waitForDenmSRsp()

# Serial config
ser = serial.Serial("/dev/ttyUSB0",115200,timeout=30)

# Main loop
while(1):
    vehicles_id = []
    sendAT_Cmd(ser,'camReceiving 15000\r',1)
    print("Info: CAM messages received successfully and "
        +str(len(vehicles_id))+" vehicles are detected!\n")
    if(Event_flag):
        denm_cmd = ('denm_event_send 15000 1000 '+demo_event.get_cmd()+'\r')
        print(denm_cmd)
        sendAT_Cmd(ser,denm_cmd,0)









