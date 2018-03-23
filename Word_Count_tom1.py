import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    
    # get the data from the url and take it is plain text
    source_code = requests.get(url).text
    soup_object = BeautifulSoup(source_code,'html.parser')
    
    for post_text in soup_object.findAll('a',{'class':'name_of_the_class'}):
        # Means, only get the string, do not care about html content.
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
           # print(each_word)
            word_list.append(each_word)
     
    clean_up_list(word_list) 
     
# this 'list' is gonna be complete list that is above 'word_list'     
def clean_up_list(list):
    clean_word_list = []
    
    for word in list:
        symbols_to_avoid = "!@#$%^&*()_+{}:\"<>?,.'[]-='" 
        
        for i in range(0,len(symbols_to_avoid)):
            
            # This below line will replace the abnormal symbols from a word with
            # blank i.e.""
            word = word.replace(symbols_to_avoid[i],"")
            
        # This is the case of ":)" because if we remove this then we will get 
        # an empty string in place of word.    
        if(len(word) > 0):
            print(word)
            clean_word_list.append(word)
    
    create_dictionary(clean_word_list)
    
def create_dictionary(list):
    # This is our blank dictionary
    word_count = {}
    
    for word in list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    # Now, we want to sort our dictionary.
    # key inside the parameter of sorted() is actually by which we want sorting
     # to occur.
    # If we want to refer to key then we pass 0 and if we wanna refer to value
     # then we will pass 1 . 
    for key, value in sorted(word_count.items(),key = operator.itemgetter(1)):
        print(key,value)
        
                                      
            
start('pass_the_url')            
            
         
        
    
    