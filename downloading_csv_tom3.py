# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 23:47:38 2016

@author: Noob
"""

# This is the python program to download and copy a csv file

# This is same as,    import urllib.request 
from urllib import request

url_link = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents-financials.csv'
def download_data(link):
    response = request.urlopen(link)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest = r'I:\\Programming\\Python_Practice\test_files\\data_downloaded_file1.txt'
    fx = open(dest,"w")
    
    for line in lines:
        fx.write(line + "\n")
        
    fx.close()

download_data(url_link)
print("Download csv file data and then writing that data is complete....")
# This program for downloading a csv file is successful.
# Keep trying more new things.    