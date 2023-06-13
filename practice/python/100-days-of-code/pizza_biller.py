print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
      # S = 15, M = 20, L = 25
      # pepperoni for M or L = 3
      # extra cheese for any = 1

size_cut = size.lower()

bill_with_pepperoni = 0

bill_with_cheese = 0

pizza_price = 0

final_bill = 0

if size_cut == "s":
    pizza_price = 15

    if add_pepperoni.lower() == "y":
        bill_with_pepperoni += 2

elif size_cut == "m":
    pizza_price = 20

    if add_pepperoni.lower() == "y":
        bill_with_pepperoni += 3

elif size_cut == "l":
    pizza_price = 25

    if add_pepperoni.lower() == "y":
        bill_with_pepperoni += 3

if extra_cheese.lower() == "y":
    bill_with_cheese += 1

final_bill = pizza_price + bill_with_pepperoni + bill_with_cheese

print(f"Your final bill is: ${final_bill}.")
