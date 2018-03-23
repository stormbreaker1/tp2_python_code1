# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 15:56:05 2016

@author: Noob
"""

# This program will not work as we do not have any pages on the website which we
# are crawling.

# Whenever we will be web related matters, we need this module
import requests 

# bs4 pacakge is installed in canopy
# bs4 is also needed for reading html data.
from bs4 import BeautifulSoup

def trade_spyder():
    url = 'https://thenewboston.com/videos_business.php'
    source_code = requests.get(url)
    plain_text = source_code.text
    
    # Converting plain_text into beautiful soup object.
    soup_object = BeautifulSoup(plain_text,'html.parser')
    
    # Getting all the titles which are in href and have class 'top-course-title'
    # We can get the class by using inspect tool of browser.
    for title in soup_object.findAll('td',{'class':'top-course-title'}):
        href = title.get('href') # href will give link 
        print(href)
            
trade_spyder()            