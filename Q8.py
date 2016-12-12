#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""
"""
8. You are given the lengths of three sides of a triangle by the user input. You should write a function that will calculate the area of this triangle with using the length of sides. There is a mathematical formula related to this.
"""

###start python code for question 8
import math
def triange_area(side1, side2, side3):
  #Heron's formula 
  #perimeter = s = (a + b + c) / 2
  #area = √(s(s-a)(s-b)(s-c))
  s = (side1 + side2 + side3) / 2
  print ""
  print "Triangle area is " + str(math.sqrt((s * (s - side1) * (s - side2) * (s - side3))))
  
while True :
  try:
        input_side1 = int(raw_input('Enter an integer for side1: ').strip())        
        if input_side1 < 0 :
            print "Please enter a posititve integer!\n"
            continue
        break
  except ValueError:
         print("Please enter an integer, NOT STRING!\n")

while True :
  try:
        input_side2 = int(raw_input('Enter an integer for side2: ').strip())
        if input_side2 < 0:
            print "Please enter a posititve integer!\n"
            continue
        break
  except ValueError:
         print("Please enter an integer, NOT STRING!\n")

while True :
  try:
        input_side3 = int(raw_input('Enter an integer for side3: ').strip())
        if input_side3 < 0:
            print "Please enter a posititve integer!\n"
            continue
        #side3 has to bigger than the other sides
        elif not input_side3 > input_side1:
            print "Side3 has to bigger than side1!\n"
            continue
        elif not input_side3 > input_side2:
            print "Side3 has to bigger than side2!\n"
            continue
        print "side1:" + str(input_side1)
        print "side2:" + str(input_side2)
        print "side3:" + str(input_side3)
        triange_area(input_side1 , input_side2 , input_side3)
        break
  except ValueError:
         print("Please enter an integer, NOT STRING!\n")
###end python code for question 8
