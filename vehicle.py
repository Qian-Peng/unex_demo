#!usr/bin/python3.6
import serial
import sys
import os
import time
import re


MAX_LOOP_NUM = 100000

def broadcast_denm():
    pass


def waitForDenmRRsp():
    maxloopNum = 0
    while True:
        line = ser.readline().decode()
        maxloopNum = maxloopNum + 1       
        try:
            print("Rsponse : "+line)
        except:
            pass
        # todo: add rebroadcast algorithm
        #if(re.search(r'recv denm count',line)):
        #    broadcast_denm()           
        if ( re.search(r'successfully',line)):
            break
        elif(maxloopNum > MAX_LOOP_NUM):
            sys.exit(0)

def waitForCamSRsp():
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

def sendAT_Cmd(serInstance,atCmdStr,waitforSuccess):
    print("Command: %s"%atCmdStr)
    serInstance.write(atCmdStr.encode('utf-8'))
    #or define b'string',bytes should be used not str
    if(waitforSuccess == 1):
        waitForCamSRsp()
    else:
        waitForDenmRRsp()

ser = serial.Serial("/dev/ttyUSB0",115200,timeout=30)
while(1):
    sendAT_Cmd(ser,'camSendingMandatory 2000\r',1)
    sendAT_Cmd(ser,'denm_event_recv 2000\r',1)


