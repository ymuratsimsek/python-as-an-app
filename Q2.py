#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:38 2016

@author: ymuratsimsek
"""
"""
2.You are given a long sequence of DNA code. You are responsible to record and print the number of occurences of “ATG” codes specifically that are important for determination of the gene sites. Then you need to insert the string “x” in front of and at the end of these strings in order to make them noticed more easily. For instance, the string “...AATGCC...” should be converted to “...AxATGxGCC...”. Here is the whole string:
    ‘AATCGGCATGCCGAATTTCCGCTATGTTGCATGCATCGTACGATGCATATGCATAGAGGGCTTTTAACGATGCCCGATGATTTCATGCCCGTAACGACTCTGACGTACTG’
Then you should clean the x’s you provided in the data. Finally you need to report the number of nucleotides that are A, T, G, C in this sequence.
"""

###start python code for question 2
dna = "AATCGGCATGCCGAATTTCCGCTATGTTGCATGCATCGTACGATGCATATGCATAGAGGGCTTTTAACGATGCCCGATGATTTCATGCCCGTAACGACTCTGACGTACTG"
dna_x = dna.strip().replace("ATG","xATGx")
print "DNA with x to noticed more easily: " + dna_x
print "number of A in DNA: "+ str(dna.count("A")) 
print "number of T in DNA: "+ str(dna.count("T"))
print "number of G in DNA: "+ str(dna.count("G"))
print "number of C in DNA: "+ str(dna.count("C"))

###end python code for question 2
