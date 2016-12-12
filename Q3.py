#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""
"""
3. You are given a list of names below. You should be counting and printing the number of items that includes the letter “a” regardless of its occurrences in an item. For instance: the list including ‘Utku’, ‘Aynur’, ‘Tarık’, and ‘Aktan’ includes 4 a’s but 3 items in the list include a. Thus, you need to report both of these cases.
nameList = ["Utku", "Aynur", "Tarik", "Aktan", "Asli", "Ahmet", "Metin", "Funda", "Kemal", "Hayko", "Zelal", "Kenan", "Asli", "Atakan", "Umut"]
You need to be careful about the case-sensitive feature of python. If you count a’s in Aktan, there will be one and for A’s the result will be the same. However, the output for the occurence of a is 2. You can make use of for-loops to go over the whole list quickly. You should print both the total number of a’s and the total number of names including the target letter, a.
"""

###start python code for question 3
nameList = ["Utku", "Aynur", "Tarik", "Aktan", "Asli", "Ahmet", "Metin", "Funda", "Kemal", "Hayko", "Zelal", "Kenan", "Asli", "Atakan", "Umut"]

total_a_count = 0
total_a_in_name_count = 0

for letter in nameList :
    if "a" in letter.lower() :
        total_a_count = total_a_count + letter.lower().count("a")
        total_a_in_name_count = total_a_in_name_count + 1

print "The Total Number of a’s: " + str(total_a_count)
print "The Total number of names including the target letter, a: "+ str(total_a_in_name_count)
###end python code for question 3
