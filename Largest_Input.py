#Write an app that inputs a series of 10 integers and determines and prints the larget integers. 
#Your app should use at least the following three variables:
#1-Counter: a counter to count to 10(e.g. to keep track of how many numbers have been input and to determine when all 0 numbers have been processed).
#2-Number: the integer most recently input by the user.
#3-Largest: the largest number found so far.


class Largest(object):
	def __init__(self):
		pass
	def determineLargest(self):
	    largest = int(input("Enter a number: "))
	    counter = 1

	    while counter<10:
	        number = int(input("Enter a number: "))
	        if number > largest:
	            largest = number
	        counter= counter+1
	    print("Largest number is " + str(largest))        	


largest = Largest()
largest.determineLargest()