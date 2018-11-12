# One of the air cargo companies raises its prices as follows:
# If the transport distance is less than or equal to 1000 miles, the cost will be calculated through the following table:
#
#
# Weight in tones (W)                        Types Of Services
#
#                                 Miscellaneous goods       Containers
#  
#        W<=50                           $100/ton             $150/ton 
#       50<W<200                         $200/ton             $250/ton
#        W>=200                          $300/ton             $350/ton
#
#
# If the transport distance is grater than 1000 miles, the cost of shipping will be calculated using the following equation:
#    cost = 10 W + 5 ln(transport distance)
#
# Write a script that calculates the total cost of shipping, which depends on the type of service provided, weight and transport distance


def calculateCostLessThan_1000(weight,serviceType):
	cost = 0
	if serviceType == 1:
		if 0<weight <= 50:
			cost = 100 * weight
		elif 50 < weight < 200:
		    cost = 200 * weight
		elif weight >= 200:
		    cost = 300 * weight
		else:
		    print("weight must be grater than zero")
	elif serviceType == 2:
		if 0< weight<= 50:
			cost = 150 * weight
		elif 50 < weight < 200:
			cost = 250 * weight
		elif weight >= 200:
			cost = 350 * weight
		else:
			print()
	else:
		print("service type must be 1 for Miscekkaneous goods OR 2 for Containers")
	return cost



distance = int(input("please insert distance: "))

if  0 < distance <= 1000:
	serviceType = int(input("Please specify the type of service (Miscellaneous goods or Containers:) Type 1 or 2: "))
	weight = int(input("Please insert the weight in tons: "))
	cost = calculateCostLessThan_1000(weight,serviceType)
	print("total cost is $"+ str(cost))
elif distance > 1000:
	weight = int(input("Please insert the weight in tons: "))
	cost = 10*weight + 5 * distance
	print("total cost is $"+ str(cost))
else:
	cost = 0
	print("ditance must be grater than 0")



















