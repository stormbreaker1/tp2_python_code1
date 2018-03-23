# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:48:04 2016

@author: Noob
"""

# This program is not working.....
# threading is a module and Thread is a class
# A module can have many classes.
import threading

# parent class is Thread
class thread_messanger(threading.Thread):
    # run() is a method just like in java which will be the only method to be
    # implemented
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
        
xobj = thread_messanger(name='send out messages \n')
print('\n')
yobj = thread_messanger(name='receives messages \n')
print('\n')

xobj.start()
yobj.start()        