#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""

"""
1. Please get the name and surname of the user. Whatever user enters his/her name & surname, your code should convert it in a regular form. For instance, alan smith should be converted to “Alan Smith” by your code. Then gender of the user should be asked separately and user’s response (M/F) should be obtained. If the gender of the user is male, you should be welcoming him as “Hello, Mr. XXXX”, if female “Hello, Mrs. XXXX”. Hint: You need to make use of if-else statements as examplified below.

if (gender==”M”):
Do_this_1....
if (gender==”F”):
Do_this_2....
"""

###start python code for question 1
user_name_surname = raw_input('Enter Your Name & Surname Please: ')

#check the input has leading and ending whitespaces/blanks?
if user_name_surname != user_name_surname.strip():

   #removing leading, middle and ending whitespaces/blanks by strip(),join() and split() functions
   #making uppercase the first char of each strings by title() function 
   user_name_surname = " ".join(user_name_surname.strip().title().split())
   print user_name_surname.strip().title().split()
   #assigning the name and surname
   name = user_name_surname.strip().title().split()[0]
   surname = user_name_surname.strip().title().split()[-1]

else :
   #removing leading, middle and ending whitespaces/blanks by strip(),join() and split() functions
   #assigning the name and surname
   user_name_surname = " ".join(user_name_surname.strip().title().split())
   name = user_name_surname.strip().title().split()[0]
   surname = user_name_surname.strip().title().split()[-1]
   
user_gender = raw_input('Enter Your Gender like M for male, F for female: ')

#check the input, is it proper or not?
if (user_gender.strip().lower() == "male") or (user_gender.strip().lower() == "m") :
   user_gender = "M"
   
elif (user_gender.strip().lower() == "female") or (user_gender.strip().lower() == "f") :
   user_gender = "F"

else :
   user_gender = raw_input('Please Enter A Proper Gender M/F: ')
   if (user_gender.strip().lower() == "male") or (user_gender.strip().lower() == "m") :
       user_gender = "M"
   elif (user_gender.strip().lower() == "female") or (user_gender.strip().lower() == "f") :
       user_gender = "F"

if user_gender == "M" :
   print '"Hello, Mr. '+ user_name_surname.title() + '"'
   print '"Hello, Mr. '+ surname.title() + '"'

else :
  print '"Hello, Mrs. '+ user_name_surname.title() + '"'
  print '"Hello, Mrs. '+ surname.title() + '"'
###end python code for question 1
