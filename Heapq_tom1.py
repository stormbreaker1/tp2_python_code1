# Helps in finding largest and smallest

import heapq

list1 = [3,4,7,5,6,8,11,12,24,35,75,57]

# First parameter tells hte number of items we want and second argument tells 
 # the list from which we want largest or smallest
print(heapq.nlargest(3,list1))