# welcome to the bill splitter
print("Welcome to the bill splitter")
print("This program will help you split the bill between friends")

totalBill = float(input("Please enter the total bill amount: "))
noOfPeople = int(input("Please enter the number of people to split the bill: "))
tipPercentage = int(input("Please enter the tip percentage: "))
tipAmount = (tipPercentage / 100) * totalBill
totalBill += tipAmount
perPersonSplit = totalBill / noOfPeople
print(f"The total bill amount is: {round(totalBill, 2)}")
print(f"The tip amount is: {round(totalBill, 2)}")
print(f"The tip amount is: {round(tipAmount, 2)}")
print(f"Each person should pay: {round(perPersonSplit, 2)}")
print("Thank you for using the bill splitter")
print("Have a nice day")

# This program is a simple bill splitter that takes the total bill amount, number of people, and tip percentage as input. It calculates the total bill amount including tip and splits it among the people. The program then displays the total bill amount, tip amount, and the amount each person should pay.
# The program uses the round function to round the amounts to 2 decimal places for better readability.