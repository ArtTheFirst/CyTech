print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 馃毃 Don't change the code above 馃憜

#Write your code below this line 馃憞
# S = 15, M = 20, L = 25
# pepperoni for M or L = 3
# extra cheese for any = 1

size_cut = size.lower()

bill_with_pepperoni = 0

bill_with_cheese = 0

pizza_price = 0

final_bill = 0

if add_pepperoni.lower() == "y":

    if size_cut == "s":
        
        bill_with_pepperoni += 2

        pizza_price = 15
        
    elif size_cut == "m":
        
        bill_with_pepperoni += 3
        
        pizza_price = 20

    elif size_cut == "l":
        
        bill_with_pepperoni += 3

        pizza_price = 25

if extra_cheese.lower() == "y":
    bill_with_cheese += 1

final_bill = bill_with_pepperoni + pizza_price + bill_with_cheese

print(final_bill)

