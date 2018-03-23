# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:45:28 2016

@author: Noob
"""

class Class_tom1:
    eyes = "blue"
    height = 178
    
    # making method inside a class, first parameter has to be "self"
    def this_method(self):
        return 'Hey! This method works'

# creating an object from the class.
object1 = Class_tom1()

# We have to print the values here also as we do in java.

# Every object have a differebt copy of the variables and methods as variables
  # here are not static as we define in java.  
print(object1.eyes)
print(object1.height)        
print(object1.this_method())