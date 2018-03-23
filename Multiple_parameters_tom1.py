# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 22:13:05 2016

@author: Noob
"""

#This is the program for multiple parameters

# This is with the single variable of multiple type.
def naam(*names):
    print (names)

# This is with two variables, one normal and other as multiple type.    
def tournament_dates(name,*age):
    print (name)
    print (age)
    
#Calling a both the fucntions
naam("meliodas","elizabeth")
tournament_dates("Soccer league", 5,6,7,8)    
    
# That parameter with * gives us tuples.qq