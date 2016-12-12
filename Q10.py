#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""
"""
10. You are given a string of integers, for instance ‘685381345973’ and you are asked to find the largest number with three digits in this sequence. This number should be found from the successive items. For instance, 973 is the largest number that you can find in the given sequence but not 988 since its items (9, 8, 8) are collected from different locations. Your code should handle any given string by the user.
"""

###start python code for question 10
while True :
  try:
        var1 = int(raw_input('Enter sequence of integers : ').strip())        
        if var1 < 0 :
            print "Please enter a posititve integer!\n"
            continue
        break
  except ValueError:
         print("Please enter an integer, NOT STRING!\n")

var2 = []
#appending every sequence in list
for x in range(len(str(var1))):
   if (x  < range(len(str(var1)))[-2]):
        var2.append(str(var1)[x] + str(var1)[x+1] + str(var1)[x+2])
        x = x + 1
#sorting the list     
print "The sorted list is " + str(sorted(var2))
print "The largest number is " + str(max(var2))
###end python code for question 10
