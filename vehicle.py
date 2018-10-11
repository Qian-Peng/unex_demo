#!usr/bin/python3.6
import serial
import sys
import os
import time
import re


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

def sendAT_Cmd(serInstance,atCmdStr,waitforSuccess):
    print("Command: %s"%atCmdStr)
    serInstance.write(atCmdStr.encode('utf-8'))
    #or define b'string',bytes should be used not str
    if(waitforSuccess == 1):
        waitForCmdOKRsp()
    else:
        waitForCmdRsp()

ser = serial.Serial("/dev/ttyUSB0",115200,timeout=30)
sendAT_Cmd(ser,'camReceiving 10000\r',1)
ser.close()