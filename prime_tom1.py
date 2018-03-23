# This program is for finding the prime in certain range....

my_num = int(input("Enter the number to be tested as prime number....\n"))


# for i in range(2,my_num):


half_my_num = int(my_num/2)

flag = 0


if my_num <= 1:
	while my_num <= 1:
		print("please enter the number greater than 1")
		print("")
		my_num = int(input("Enter the number to be tested as prime number....\n"))
		print("")

else:
	for x in range(2,half_my_num) :

		if half_my_num == 2:
			print("Entered number is not a prime number")
			flag = 1
			break

		my_mod = my_num % x

		if my_mod == 0:
			flag = 1
			break


if flag == 1 :
	print("Entered number is not a prime number....")

else :
	print("Entered number is a prime number....")


		
