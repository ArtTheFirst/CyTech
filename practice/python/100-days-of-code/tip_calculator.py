#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = 150
persons = 5
tip = (12 / 100) * bill

print(f"Your bill is ${bill}")

print(f"There are {persons} of you")

split_bill = (bill + tip) / persons

print(f"You each tipped ${tip / 5}")

final_bill = round(split_bill, 2)

print(f"Your total bill is ${final_bill * 5}")

print(f"Your are to pay ${final_bill} each.")

