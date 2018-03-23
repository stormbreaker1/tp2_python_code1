
# This program is for testing the for loop in the python

name1 = input("Please enter your name \n")

if name1 == 'kuldeep':
	print("Letters in your name are as follows \n")

	for letter in name1:
		print(letter)

	prog_langs = ['java','python','R','scala','shell']

	print("")
	print("List of all the programming languages known by you are:- ")	

	for lang in prog_langs:
		print(lang)

else:
	print("You are not kuldeep")	


print("")

print("Now is the time for knowing about the technologies you know")

print("")

print("Please verify your identity again")

id_name1 = input("Please tell me your alias name  \n")

print("")
if id_name1 == 'storm breaker' :
	print("welcome " + id_name1 + " again")


	my_tech = ['bigdata','data science','machine learning','programming']

	print("You know these technologies:- ")
	print("")

	for index in range(len(my_tech)) :
		print("You know " + my_tech[index])



	# Applying the while loop	

	# raw_input in python 2.x was also a way to receive the input from the user
	# raw_input do not evaluate the input and hence it consider it as string only....
	# input  will evaluate the entered string. 5+7 as 12

	# In 3.x , input do not evaluate the string. It consider input as string only....
	# To convert string into int here, we will use int(input("Enter the value"))


	my_count = int(input("Please provide the value for counter:- "))

	count = 0

	while count < my_count :

		# We convert the int into the string to get along with the string which we are 
		 # concatinating it with....
		print("counter value is "+ str(count))
		count = count + 1

else:
	print("You are an inpersonator, this will be reported to admin.... ")



   