# Here, we are gonna work with lists in python....

my_lang_lists1 = ['java','R','scala','shell','python']

print("My known languages are:- \n")

for lang in my_lang_lists1:
	print(lang)


print()
print("My known languages are:- \n")

# Another way of accessing the list is 
for x in range(0,len(my_lang_lists1)):
	print(my_lang_lists1[x])


# Just like in R we have a function to know about the data type as class()
# In python we have a function called as type()
print()
print("Data type of my_lang_lists1 is :- ",type(my_lang_lists1))

# List can be accessed in the reverse order as well
print()
print("List in the reverse order is as follows:-")

# We have to add plus 1 into the length because we want to include the excluded index in the 
 # normal for loop as well....
for y in range(1,(len(my_lang_lists1)+1)):
	print(my_lang_lists1[-y])



def login(name):
	if name == 'kuldeep':
		print("Welcome %s " %(name))

	else:
		# return nothing will take us out of function....
		return 

name = input("Enter your login name \n")

login(name)			

print("Program has End......")



print("We are working with the second list now.....")

my_list2 = ['hello','how','are','you','?']

# This will give added result but it will not actually affect the real my_list2 
my_list2 + ['sup?']

print(my_list2)

# We can really add the element in the existing listing by following syntax
my_list2.append('sup?')

print(my_list2)


# many values can be updated as well
# index 0,1 and 2 will get replaced by the given values in the list
# First element i.e. element at 0 index will get deleted.... 
my_list2[:3] = ['','yo','meh']

print("Printing the second list using for loop:--  ")

for x in my_list2:
	print(x)

new_ele = input("give another value \n")	

if new_ele != '':
	my_list2[2] = new_ele
else:
	pass

print("")
print("Printing the new list....")

for x in my_list2:
	print(x)


# Now, deleting an element from the list2
del my_list2[0]

print("")
print("Printing second file again after some deletion")

for x in my_list2:
	print(x)

print("")
print("Basic list operations on the lsit....")

print("Length of the list my_list2 is ",len(my_list2))


print("")


# ============================================ TUPLES =================================================== #
# Defining a tuple
my_tuple = ('hello','how','are','you?')

print("Printing the elements of tuple:- ")
for x in my_tuple:
	print(x)

print("")
print(type(my_tuple))

print("")	


print("")
print("Converting the tuple into the list")
my_new_list1 = list(my_tuple)

print("")
print("Type of my_new_list1 is ",type(my_new_list1))

print(my_new_list1)


print("Accessing the first element of the tuple....")
print(my_tuple[0])


# Trying to reassing the element inside a tuple
# It will give error as we can't change the value in tuple
# my_tuple[0] = 'yo'


# Adding extra element in the tuple
# We can't add extra element in a tuple also.... 
'''my_tuple[4] = 'yo'
print("")
print("The value at 4th index in my_tuple is",my_tuple[4])'''


print("")
my_tuple2 = 'a','b','c','d'

print("my_tuple2 values are \n",my_tuple2)
print("\nThe type of my_tuple2 is ",type(my_tuple2))


my_empty_tuple1 = ()
my_singleton_tuple = (24,)

print("\nThe length of my_empty_tuple1 is",len(my_empty_tuple1))

# Good way of concatinating the string....
print("\nThe length of my_singleton_tuple is",len(my_singleton_tuple),"and it's type is",type(my_singleton_tuple))



# But, tuples can be used to create other tuples....

# Tuples can be deleted as below
del my_tuple2

print("my_tuple2 elements are")

# It will give an error that my_tuple2 is not defined....
# print(my_tuple2)

my_tuple3 = ('yo',2,3,4,5,6,7,8,9,'xyz')

print("The elements in the my_tuple3 are\n",my_tuple3)


print("")

my_input = input("Enter any element from above:-")

if type(my_input) == 'str':

	if  my_input in my_tuple3:
		print("%s is in my_tuple3" %(my_input))
	else:
		print("%s is not in the my_tuple3"%(my_input))

elif type(my_input) == 'int':
	my_input = int(my_input)
	if my_input in my_tuple3:
		print("%d is in my_tuple3"%(my_input))
	else:
		print("%d is in my_tuple3"%(my_input))
		
else:
	pass
		
