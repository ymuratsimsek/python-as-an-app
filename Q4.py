#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""
""""
4. You should write the necessary code to obtain input from the users. The input should be a positive integer. Then your code should ask if the user wants to see the even or odd numbers. Then your code should demonstrate all of the even/odd numbers on the screen. For instance, if the user enters 7 and even as his/her choice, then your code should provide the following output:
The even numbers up to 7
2
4
6
Hints: You need to make use of if-else statements. You can make the use of for-loops or while-loops. In order to have the raw_input as integer you need to convert it afterwards like this: A = int(raw_input(‘......’)
"""

###start python code for question 4
while True :
  try:
        input_integer = int(raw_input('Enter a positive integer: '))
        #check until user enter proper input: is the input positive integer?
        if input_integer < 0 :
            print "Please enter a posititve integer!\n"
            continue
        break
  except ValueError:
         print("Please enter a posititve integer, NOT STRING!\n")

while True :
        input_even_odd = raw_input('Enter even or odd: ')
        #check until user enter proper input: is the input even or odd?
        if (input_even_odd.lower() == "even"):
            print "Your number is " + str(input_integer) + "and you said " + input_even_odd
            for x in xrange(2, input_integer+1,2):
                print x            
            break       
        elif (input_even_odd.lower() == "odd"):
            print "Your number is " + str(input_integer) + "and you said " + input_even_odd
            for x in xrange(1, input_integer,2):
                print x
            break
        else:
            print "Please enter a proper answer like EVEN or ODD! \n"
            continue
###end python code for question 4
