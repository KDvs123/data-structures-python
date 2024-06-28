# Exercise 3

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

maxNum=int(input("Enter a number between 1 to 100"))

oddNum=[]

for i in range(1,maxNum+1):
    if i%2!=0:
        oddNum.append(i)
    

print("Odd Numbers are ", oddNum)