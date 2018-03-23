# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:57:05 2016

@author: Noob
"""

# This is the program for checking default parameters

def saying(title = "respected", name = "sir"):
    print ("Hello! " + title + " "+ name + ", welcome")
    print ("Hello! %s %s, welcome"%(title,name))
# These above are the two ways of printing something.    
    
saying("demon prince","meliodas")    
saying()