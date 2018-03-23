# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 18:34:35 2016

@author: Noob
"""

# Here we are not getting any syntax error bcoz we do not have any
# But, on entering a string we will get exception. 
while True:
    try:
        number = int(input("Enter a number..."))
        print(100/number)
        break
    except ValueError:
        print("Enter the right value")
    except ZeroDivisionError:
        print("Do not give value as 0")
    except:
        break # take the interpreter outta everything.
    finally:
        print("Code Complete...") # This finally block will always run no matter what.
        
