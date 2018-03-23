# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:10:29 2016

@author: Noob
"""
# This is the program to get dictionary as parameter in pythons
def full_name(**name):
    print(name)
    
# This will print all the things in dictgionary format.
# While passing as parameter we need to use "=" sign, but we will get the result
  # as ":" form.

# in case of passing a whole dictionary as parameter inside the function, we
  # should not give '' in key and we should use "=" sign instead of ":"     
full_name(demon="melidas",angel="elizabeth")

# full_name(demon=melidas,angel=elizabeth), this will not work.    

# Now we are gonna pass an already defined tuple in the function

def points(*num):
    print(num)
 
tup = (2,3,4,5,6)

points(*tup)

# Data for the dictionary
dictionary1 = {'Ind':4,'Aus':1}
# Use '' for key and to differentiate key and value we will use "". 
dictionary2 = {'Name':"meliodas",'Race':"Demon"}
full_name(**dictionary1)
full_name(**dictionary2)
