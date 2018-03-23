# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 00:53:55 2017

@author: Noob
"""

import random

# This is same as,   from urllib import request
import urllib.request

def download_image(url):
    image_name = random.randrange(1,100000000)
    full_name = str(image_name) + ".jpg"
    
    # 2nd argument is for with which name we wanna save the downloaded image
    urllib.request.urlretrieve(url,full_name)
    
    # End of the function
    
download_image("http://3.bp.blogspot.com/-_qpmdZfw9jM/UajNNnJ7hzI/AAAAAAAAbQE/MRCTBYT3xeY/s1600/harold+finch+07.jpg")    
print("Image Successfully downloaded and saved")