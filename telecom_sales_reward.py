## A telecom company wants to reward 10 salespersons for selling the company phone lines based on the following table
##
## phone lines       reward per phone line
##                  residential    business
##   0 - 50              $10          $15
##  51 - 100             $15          $20
##    > 100              $20          $25
# write a script to compute the total reward for one salesperson
# the script first asks the user to enter number of residential & business lines sold
#then it computes the reward. The max reward for any salesman can not exceed $7500



print("Welcome to Salesperson reward system")
print("###################################")
print("")
residential_lines_sold = int(input("enter number of residential lines sold: "))
business_lines_sold =  int(input("enter number of business lines sold: "))
residential_reward = 0
business_reward = 0
total_reward = 0


# residential lines sold
if residential_lines_sold > 0:
	if residential_lines_sold <= 50:
		residential_reward = residential_lines_sold * 10
	elif 51 <= residential_lines_sold <= 100:
	    residential_reward = residential_lines_sold * 15
	else:
	    residential_reward = residential_lines_sold * 20
else:
    residential_reward = 0

#  business lines sold
if business_lines_sold > 0:
	if business_lines_sold<= 50:
	    business_reward = business_lines_sold * 15
	elif 51 <= business_lines_sold <= 100:
	    business_reward = business_lines_sold * 20
	else:
	    business_reward = business_lines_sold * 25
else:
	business_reward = 0

#total reward calculation
total_reward = residential_reward + business_reward


#check if total reward > 7500
if total_reward > 7500:
	total_reward = 7500
	print("total reward cannot be grater than 7500 monthly therefore, your total reward this month is: $" + str(total_reward))
else:
	print("residential reward: $"+str(residential_reward))
	print("business reward: $"+ str(business_reward))
	print("total monthly reward: $"+ str(total_reward))



