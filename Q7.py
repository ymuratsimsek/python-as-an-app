#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""
"""
7. We all know that the area of a triangle can easily be calculated if the height and the base are given. You will get the inputs for these parameters from the user. Then your code should calculate and print the area of this triangle. You can either do it with a function or not. The area formula is: (height * base)/2
"""

###start python code for question 7
def triange_area(base, height):
  print ""  
  print "Triangle area is " + str((base * height) / 2)
  
while True :
  try:
        input_base = int(raw_input('Enter an integer for base: ').strip())        
        if input_base < 0 :
            print "Please enter a posititve integer!\n"
            continue
        break
  except ValueError:
         print("Please enter an integer, NOT STRING!\n")

while True :
  try:
        input_height = int(raw_input('Enter an integer for height: ').strip())
        if input_height < 0:
            print "Please enter a posititve integer!\n"
            continue
        triange_area(input_base , input_height)
        break
  except ValueError:
         print("Please enter an integer, NOT STRING!\n")
###end python code for question 7
