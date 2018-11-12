#Wrtie an application to simulate the rolling of two dice. The app should use an object of class Random once to roll the first die 
#and again to roll the second die. The sum of the two values should then be caluculated.
#Each die can show an integer value from 1 to 6, so the sum of the values will vary from 2 to 12, 
#with 7 being the most frequent sum and 2 and 12 being the least frequent sums. 
#The Figure shows the 36 possible combinations of the two dice. Your app should roll the dice 36000 times.
#Use a one dimensional array ti keep trck of the number of times each possible sum appears. 
#Display the result in a tabular format. determine whether the totals are reasonable 
#(e.g., there are six ways to roll a 7, so approximately one-sixth of the rolls should be 7).

#     1   2   3   4   5   6
# 1   2   3   4   5   6   7
# 2   3   4   5   6   7   8
# 3   4   5   6   7   8   9
# 4   5   6   7   8   9   10
# 5   6   7   8   9   10  11
# 6   7   8   9   10  11  12

#Hints:
#1-Keep track of how many times each total(2 through 12) occurs. This total is used to calculate the percentage of the time that each total occurs.
#2-Define a loop that iterates 36,000 times. during each iteration, roll the dice, 
#calculate the total and update the count for the particular total in the array.
#3-create an array large enough that you can use the sum of the dice as the index into the array.
#4-Your output should appear as follows:
# sum    frequency    percentage
#  2        1027          2.85
#  3        2030          5.64
#  4        2931          8.14
#  5        3984          11.07
#  6        5035          13.99
#  7        5996          16.66
#  8        4992          13.87
#  9        4047          11.24
#  10       2961          8.23
#  11       1984          5.51
#  12       1013          2.81


import random

counter=0
frequency = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
percentage = {}
total_frequency=0
total_pecentage=0

#find frequency of occurange for each sum of dice
while counter < 3600:
	dice_1=random.randrange(1,7,1)
	dice_2=random.randrange(1,7,1)
	sum = dice_1 + dice_2

	if sum in frequency:
		frequency[sum] = frequency[sum]+ 1
	else:
	    frequency[sum] = 1
	counter+=1

#find percenatage of occurrance for each frequency
for i in frequency:
	caluclate_percentage = (frequency[i]/3600)*100
	formated_percentage = round(caluclate_percentage,3)
	percentage[i] = formated_percentage


#print result
#print header
print("sum "+  "  frequency  " + "  percentage  ")
for i in range(2,13):
	print(" " + str(i) + "        "+ str(frequency[i]) + "         " + str(percentage[i]))
	total_frequency = total_frequency + frequency[i]
	total_pecentage = total_pecentage + percentage[i]
#print totals    
print("total    ", str(total_frequency) + "       "   + str(total_pecentage))    


