expenses=[2200,2350,2600,2130,2190];
months=["January","Februray","March","April","May"]

total=0;

# Exercise 1.1

# 1. In Feb, how many dollars you spent extra compare to January?

expenseOnJan=expenses[0]
expenseOnFeb=expenses[1]

extraSpentExpense=expenseOnFeb-expenseOnJan
print(extraSpentExpense)

# Exercise 1.2

# 2. Find out your total expense in first quarter (first three months) of the year.

for i in range(3):
    total=total+expenses[i]


print("Total expense in first quarter is: ", total)


# Exercise 1.3

# 3. Find out if you spent exactly 2000 dollars in any month

for i in range(len(expenses)):
    if(expenses[i]==2000):
        print("Yes, you spent exactly 2000 dollars in month "+months[i])

## Answer was given as this 


print("Did I spent 2000$ in any month? ", 2000 in expenses) # False


# Exercise 1.4

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

#  expenses[5]=1980 - this is giving me list assignment out of range


## answer was given as append

expenses.append(1980)


# Exercise 1.5

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

expenses[3]=1930


