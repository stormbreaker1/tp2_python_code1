# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 23:27:43 2016

@author: Noob
"""

# This is the python program to download and copy a csv file
from urllib import request

url_link = 'http://www.ibm.com/support/knowledgecenter/en/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/ComputerSystemsImportSample.csv?view=kc'
def download_data(link):
    response = request.urlopen(link)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest = r'I:\\Programming\\Python_Practice\test_files\\ibn_downloaded_file1.txt'
    fx = open(dest,"w")
    
    for line in lines:
        fx.write(line + "\n")
        
    fx.close()

download_data(url_link)
# This program for downloading a csv file is successful.
# Keep trying more new things.    