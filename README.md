# unex_demo
The program demostrates simple applications based on unex devices using v2x.  

## Introduction
'Event.py' simulates events with different features which is used by 'Monitor.py' and 'Vehicle.py'.  
'Monitor.py' simulates a traffic monitor which could recevice CAM messages from vehicles and calculate the number of nearby vehicles.
Moreover, it will send out DENM messages if it receive event signals (in the program we assume that there is an event). 
'Vehicles.py' simulates a vehicle which keeps on sending out CAM messages and detecting DENM messages from outside.

## How to run the program
1. Preparations
Two servers which have serial ports for communicating, with python3 and pyserial library installed.  
`sudo apt-get install python3`, `pip3 install pyserial` 
Two Unex devices with serial ports connected to servers above. 
Also make sure the serial port on the server is "/dev/ttyUSB0", if not, change the name in python files. 
2. Run
On one server, run `sudo python3 Monitor.py` and the other `sudo python3 vehicle.py`.
