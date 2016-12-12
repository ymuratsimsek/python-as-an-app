#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""

"""
9. You need to get the coordinates of two points from the user. A coordinate consists of x and y values such as (1,3) for (x,y). Your code should get these x-y parameters in the form of (21,34) and should assign x = 21 and y = 34 for the first point and then similarly for the second point. Your code should then calculate the distance among these points. Hint: To calculate this distance you need to use the formula of Pythagoras.
"""

###start python code for question 9
# user has to use parenthesis "()", comma "," and integer numbers like (10, 20) while entering inputs
# to check this rule above, i write this fuction below
def check_input_is_proper(): 
 while True :
        user_input = raw_input('Enter x and y point like (x,y): ')
        #input has to start with "(" if not return to beginning
        if not user_input.startswith("("):
            print "Please enter numbers like (x,y)\n"
            continue
        #input has to have "," if not return to beginning        
        elif "," not in user_input:
            print "Please enter numbers like (x,y)\n"
            continue
        #input has to end with ")" if not return to beginning
        elif not user_input.endswith(")"):
            print "Please enter numbers like (x,y)\n"
            continue
        #creating x and y after some computations like removing parenthesis, comma and index operation
        x = (''.join(user_input.replace("(","").replace(")","").split(",")[0].split()))
        y = (''.join(user_input.replace("(","").replace(")","").split(",")[1].split()))
        break

#both x and y have to be an integer if not return to beginning
 if (not x.isdigit()) and (not y.isdigit()) :
            print "Please enter intergers for x and y\n"
            check_input_is_proper()
 elif (not x.isdigit()) and (y.isdigit()) :
            print "Please enter an interger for x\n"
            check_input_is_proper()            
 elif (x.isdigit()) and (not y.isdigit()):
            print "Please enter an integer for y\n"
            check_input_is_proper()   
 return x,y

# the distance among two coordinate points is √c*c = √(x1 − x2)*(x1 − x2)  + (y1 − y2)*(y1 − y2)
import math
def distance_btw_2_points(a1,b1,a2,b2):
    dist = ((a1 - a2) * (a1 - a2) ) + ((b1 - b2) * (b1 - b2))
    print ""
    print "The distance btw 2 coord. points is: "+ str(math.sqrt(dist))

print "Getting first coordinate points:"
x1, y1 = check_input_is_proper()
print "Getting second coordinate points:"
x2, y2 = check_input_is_proper()
print "x1,y1 is : " + x1 + "," + y1
print "x2,y2 is : " + x2 + "," + y2
# convert inputs to integer
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)
#calling distance_btw_2_points function
distance_btw_2_points(x1,y1,x2,y2)
 
###end python code for question 9
