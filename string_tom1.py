# Using the string in python....

string1 = "Hey! What are you doing?"
string2 = "Hey! You are a champ in the coding...."


# Python do not support character, it consider it to be string of length of 1

# To access the substring we pass the indexes in square brackets...

print ("The first character of the string1 ",string1[0])

print ("The substring in string2 is ", string2[3:10])


# string1 will get repeated 3 times when we use * operator with the string....
print("Let us repeat the string1 3 times ",string1*3)



name1 = input("Please provide your name here on the console.... \n")


if name1 == 'kuldeep':

	# This is how we format the string in python. It is little different than java
	# In java we use,      printf("Welcome % aka storm breaker",name1)
	print("Welcome %s aka storm breaker...."%(name1))



# There are a lot of in built methods avaialble in python for string like

# capitalize(), center(), count(), 

print("Your name's length is ",len(string1))


# Capitalizing the string1

# This below code will capitalize only first character of your string....
print("string1 after capitalizing is:- ",string1.capitalize()) 


string3 = "pied piper"

# center() method of the string is use to center the string around some character
# Second argument must be single character only.... 
print("pied piper is centered around a as :-", string3.center(100,'g'))



# For getting the number of occurrence of a sub string in a string....
# It's kinda regular expression in java....
string4 = 'Hey what are you what are who are you?'

sub_str1 = input("Please provide the substring to be searched \n")

if sub_str1 == 'you':
	print("your substring is %s and it occurred for %d times" %(sub_str1,string4.count(sub_str1,0,len(string4)) ) )

elif sub_str1 == 'who':
	print("your substring is %s and it occurred for %d times" %(sub_str1,string4.count(sub_str1,0,len(string4)) ) )

elif sub_str1 == 'are':
	print("your substring is %s and it occurred for %d times" %(sub_str1,string4.count(sub_str1,0,len(string4)) ) )

else:
	print("You provided some unknown string....")





# Encoding the string on some encoding scheme
string5 = "Hey! Are you coming to the party?"
enc_string5 = string5.encode()

print("Encoding of %s is %s" %(string5,enc_string5))



# Decoding the string....

dec_string5 = enc_string5.decode()


# Testing if string contains numeric value or not 
string6 = 'abdh3829bnam'
string7 = '492479237848947938712'


# Checking for string6
if string6.isnumeric():
	print ("string6 have all numeric values")

else:
	print("string6 do not have all numeric values")



# Checking for string7	
if string7.isnumeric():
	print ("string7 have all numeric values")
else:
	print ("string7 do not have all numeric values")



string8 = 'dkjahdkjaRabd'

if string8.islower():
	print("All the characters of the string8 are lower cased....")
else:
	print("All the characters of the string8 are not lower cased....")


# We will be checking if all the characters of the string8 are lower or not 
# If not then we will be converting them to lower cased....
string9 = 'djahdTkdnakd'

if string9.islower():
	pass
else:
	print("All the characters of the string9 were not lower cased....")
	print()
	print("Converting the characters of the string9 into lower case....")

	string9 = string9.lower()
	print()

	print("The new string9 is ")
	print()
	print(string9)


# Using the replace() function onto the string....
string10 = 'hello! how are you? i did not see you since the last competition'

print("This is the string10 \n")
print(string10)
print()
print("Replacing the 'are' in the string10 with 'was' ....")

# Third parameter tells that maximum number of places string have to be replaced....
print(string10.replace('are','was',1))



# Using the split() function in python.... 
# split() function takes in two arguments, first with which we want to split and second with which 
 # we wanna define the number of max split....

# If nothing is specified then it will split on the bases of white spaces....
print("Spliting the string10 on the basis of white spaces \n")
print()

# This will split on the basis of white spaces....
print(string10.split())

print()
print("Spliting string10 on the basis of 'h' ")

print()

print(string10.split('h'))

print()

print("Splitting the string10 on the basis of 's' ")
print()
print(string10.split('s',3))



# Using startsWith() function
print(string10.startswith('hello'))    # It will return true
print(string10.startswith('how'))     # It will return false
print(string10.startswith('how',1))      # it will return false and second parameter tells from where to start
print(string10.startswith('are',2,8))   # It will return false, second parameter tells starting index and 3rd parameter
 # tells the ending index....
 

# Finding the indexes of the searched string inside a string
# These starting and ending indexes are the places of characters....
print(string10.find('hello'))
print(string10.find('how',0))
print(string10.find('you',11,30)) 