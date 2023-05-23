#!/usr/bin/env python3

import sys

#Initialise values
last_State = None
last_City = None
City_Count = 0
State_Count = 0
curr_State = None

for line in sys.stdin:

    #input from mapper sorted according to keys First according to States and then according to Cities
    curr_State,curr_City,count = line.split(',')
    count = int(count)

    #repeatition of same State -> increment State_Count
    if(last_State == curr_State):

        State_Count += count

        #repeatition of same City -> increment City_Count
        if(last_City == curr_City):
            City_Count += count
        else:

            #check if last_City is None -> it is the first City hence we dont print else we print City
            if(last_City != None):
                print("%s %s"%(last_City,City_Count))
            
            #Update value of last_City and City_Count to curent values seen so far
            City_Count = count
            last_City = curr_City

    else:
        #check if last_State is None -> it is the first State hence we dont print else we print State
        if(last_State != None):
            print("%s %s"%(last_City,City_Count))
            print("%s %s"%(last_State,State_Count))
        
        #print while transitioning from one state to another state
        print("%s"%(curr_State))

        #update values to new state and new city
        City_Count = count
        last_City = curr_City
        State_Count = count
        last_State = curr_State

#last state incase missed in loop
if(curr_State == last_State):
    print("%s %s"%(last_City,City_Count))
    print("%s %s"%(last_State,State_Count))