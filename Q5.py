#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""
""""
5. We did not have enough time to cover the use of functions in the class but this is a nice opportunity for us to make a slight introduction to the use of functions in python. Here is an example for the functions:
def greet(name):
print “Hello “, name
Thus, when you use the function as such, greet(‘Sarah’), the output will be ‘Hello Sarah’. In this question, you are asked to write a summation function without making the use of sum function in python, of course. The name of your function could be ‘topla_gel’ (or anything else) but it should provide the summation of the integers up to the number given by the user. If the user enters 5, the function should make the necesssary calculation, 1+2+3+4+5, and the output should be 15.
Hints: You can make the use of for-loops that we have covered in the class. Again, you code should obtain the input from the use as digit and control if there are blanks in the input, if yes please clear them.
"""

###start python code for question 5
#check until user enter proper input: is the input an integer?
def topla_gel(number):
  total = 0
  ### without using for loop: number * (number + 1) / 2
  for x in xrange(1,number+1,1):
        total = x + total
  print "Total is " + str(total)  

while True :
  try:
        input_integer = int(raw_input('Enter an integer: ').strip())       
        topla_gel(input_integer)
        break
  except ValueError:
         print("Please enter an integer, NOT STRING!\n")

###end python code for question 5
