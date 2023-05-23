#!/usr/bin/env python3

import sys
import json
import requests
from math import dist

#get the command-line-arguements
distance = float(sys.argv[3])
coord1 = [float(sys.argv[1]),float(sys.argv[2])]
attributes = ["Start_Lat","Start_Lng"]

for line in sys.stdin:

    #convert JSON string to dict object
    record = json.loads(line)

    #check for NaN values
    if(any(record[attr] != record[attr] for attr in attributes)):
        continue
    
    #get lat_lng values for each record and compute euclidean distance
    coord2 = [record['Start_Lat'],record['Start_Lng']]

    #check if computed euclidean dist within given threshold
    if(dist(coord1,coord2) <= distance):

        #populate the body of request msg
        jsonPacket = {"latitude":record['Start_Lat'],"longitude":record['Start_Lng']}

        #query server for City and State details
        res = requests.post('http://20.185.44.219:5000/',json=jsonPacket)

        #convert JSON string to dict object
        loc = json.loads(res.text)

        #print key-value pairs
        print("%s,%s,%s" % (loc['state'],loc['city'],1))