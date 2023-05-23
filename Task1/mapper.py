#!/usr/bin/env python3

import sys
import json

matchingDesc = ["lane blocked","shoulder blocked","overturned vehicle"]
matchingWeatherCond = ["Heavy Rain","Thunderstorm","Heavy Rain Showers","Heavy Snow","Blowing Dust"]
attributes = ["Severity","Sunrise_Sunset","Visibility(mi)","Precipitation(in)","Weather_Condition","Description","Start_Time"]

for line in sys.stdin:

    #convert JSON string to dict object
    record = json.loads(line)

    #check for NaN values
    if(any(record[attr] != record[attr] for attr in attributes)):
        continue

    #check which records meet the requirements
    if(record["Visibility(mi)"] <= 10 and record["Precipitation(in)"] >= 0.2 and record['Severity'] >= 2 and record['Sunrise_Sunset'] == "Night"):
        if(any(item == record['Weather_Condition'] for item in matchingWeatherCond)):
            currDesc = record['Description'].lower()
            if(any(item in currDesc for item in matchingDesc)):

                #extract hour and print key-value pair
                #keys are alphabets. A implies 0,B implies 1....Z implies 23
                #values is 1
                hourly_Key = int(record['Start_Time'].split(' ')[1][0:2])
                print("%s %s" % (chr(hourly_Key+65),1))