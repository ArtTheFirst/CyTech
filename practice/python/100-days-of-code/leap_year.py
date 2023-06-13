year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 

#Write your code below this line 
#print(year % 2)

if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        print(f"{year} is a leap year")
else:
        print(f"{year} is not a leap year")
