# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 21:57:35 2016

@author: Noob
"""

class Employee:
	# This is the constructor we are definding in here....
	# self works as 'this' in java for initializing the variables....
    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position
        
    def info(self):
        print("You are %s \n Your age is %d \n You are %s"%(self.name,self.age,self.position))
        
emp = Employee("meliodas",14,"captain")
emp.info()       
        