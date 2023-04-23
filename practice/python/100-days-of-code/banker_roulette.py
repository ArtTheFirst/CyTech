import random 


names_string = input("Enter names separated by a comma. ")

names = names_string.split(", ")

people_count = len(names)

dice_roll = random.randint(0, people_count - 1)

whos_to_pay = names[dice_roll]

print(f"{whos_to_pay} is going to buy the meal today!")
