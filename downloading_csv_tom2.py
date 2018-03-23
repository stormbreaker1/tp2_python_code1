# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 23:39:53 2016

@author: Noob
"""

# This is the python program to download and copy a csv file
from urllib import request

url_link = 'https://help.shopify.com/manual/customers/import-export-customers/#file-format'
def download_data(link):
    response = request.urlopen(link)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest = r'I:\\Programming\\Python_Practice\test_files\\ibn_downloaded_file2.txt'
    fx = open(dest,"w")
    
    for line in lines:
        fx.write(line + "\n")
        
    fx.close()

download_data(url_link)
# This program for downloading a csv file is successful.
# Keep trying more new things.    