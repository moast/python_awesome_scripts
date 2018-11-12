#A palindrome is a sequence of characters that reads the same backwards as forward. For example, 
#each of the following five-digit integers is a palindrome:
#12321, 55555, 45554, 11611. 
#Write an application that reads in a five-digit integers and determine whether it is a palindrome. 
#If the number is  not five digit long, display an eror message and allow the user to enter a new value.

# Sample Output:
# Please Enter a five-digit number:1234
# Number must be 5 digits
# Please Enter a five-digit number:123456
# Number must be 5 digits
# Please Enter a five-digit number:54345
# 54345 is Palindrome

class Palindrome(object):
	"""docstring for Palindrome"""
	def __init__(self):
		super(Palindrome, self).__init__()
		

	def checkPakindrome(self):
	    self.input_number = int(input("Please Enter a five-digit number: ")) #palindrome number to test
	    input_number_string = str(self.input_number)

	    #Write code that inputs a five-digit number, Display an error message 
	    #if the number is not five digits. Loop until a valid input is received
	    while len(input_number_string) != 5:
	    	print("Number must be 5 digits")
	    	self.input_number = int(input("Please Enter a five-digit number: "))
	    	input_number_string = str(self.input_number)

	    #Write code that separates the digits in the five-digit number. 
	    #Use division to isilate the left-most digit in the number, 
	    #use a reminder calculation to remove that digit from the number. 
	    #Then repat this process.

	    self.digits = len(input_number_string) #number of digits
	    self.digit_5 = int(self.input_number/10000) #left-most digits in the number, example: 8 is digit_5 in 83412
	    remaining_4_digits = int(self.input_number%10000)
	    self.digit_4 = int(remaining_4_digits/1000)
	    remaining_3_digits = int(remaining_4_digits%1000)
	    self.digit_3 = int(remaining_3_digits/100)
	    remaining_2_digits = int(remaining_3_digits%100)
	    self.digit_2 = int(remaining_2_digits/10)
	    self.digit_1 = int(remaining_2_digits%10)

	    #Write code that determines wether the first and the last digit are identical 
	    #and the second and fourth digits are identical.
	    #Output whether or not the original string is a palindrome.

	    if self.digit_5 == self.digit_1:
	    	if self.digit_4 == self.digit_2:
	    		print(input_number_string + " is a Palindrome")
	    	else:
	    	    print(input_number_string + " is NOT a Palindrome")
	    else:
	    	print(input_number_string + " is NOT a Palindrome")


class PalindromeTest():
	def testANumber(self):
		palindrome = Palindrome()
		palindrome.checkPakindrome()

		

palindromeTest = PalindromeTest()
palindromeTest.testANumber()





