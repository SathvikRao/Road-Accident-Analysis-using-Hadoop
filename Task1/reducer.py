#!/usr/bin/env python3

import sys

#Initialise values
prev_Hour = None
hour_Count = 0

for line in sys.stdin:
    
    #input from mapper sorted according to keys
    curr_Hour, count = line.split(' ')
    curr_Hour = ord(curr_Hour)-65
    count = int(count)
    
    #repeatition of same hour -> increment hour_Count
    if(prev_Hour == curr_Hour):
        hour_Count += count
    else:
        #check if prev_Hour is None -> it is the first hour hence we dont print else we print hour 
        if(prev_Hour != None):
            print("%s %s"%(prev_Hour,hour_Count))

        #Update value of prev_hour and hour_Count to curent values seen so far
        hour_Count = count
        prev_Hour = curr_Hour

#last hour incase missed in loop
if(prev_Hour == curr_Hour):
    print("%s %s"%(prev_Hour,hour_Count))