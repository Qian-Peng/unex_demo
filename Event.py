import sys
import time

# Define a class of Event, which simulates a real-time event 
# and provides interfaces for monitor to check status or do setups

class Event:

    station_list=["","pedestrian","cyclist","moped","motorcycle",
        "passenger car","bus","light truck","heavy truck","trailer",
        "special vehicles","tram","RSU"]
    direction_list=["all traffic directions","up stream traffic",
        "down stream traffic","opposite traffic"]
    distance_list=["less than 50m","less than 100m","less than 200m",
        "less than 500m","less than 1000m","less than 5km",
        "less than 10km","over 10km"]


    # Set id and initial time 
    def __init__(self,id,station_type,position_x,position_y,dir=0):
        self.id = id    
        self.time_tick = time.time()
        self.station_type = station_type
        self.position_x = position_x
        self.position_y = position_y
        self.dir = dir 
        self.event_flag = 1
     

    # Derive running time of traffic light
    def get_running_time(self):
        self.running_time = time.time() - self.time_tick
        return round(self.running_time,2)

    def print_status(self):
        print("Event id: "+str(self.id))
        print("Event started "+str(self.get_running_time())+" seconds before")
        print("Event object: "+self.station_list[self.station_type])
        print("Event position: ("+str(self.position_x)+","+str(self.position_y)+")")
        print("Event direction: "+self.direction_list[self.dir])
        if(self.event_flag):
            print("Event expired? No")
        else:
            print("Event expired? Yes")
        

    def get_expired(self):
        return self.event_flag


