

age = input("What is your current age? ")
# 🚨 Don't change the code above 

#Write your code below this line

#print(f"You have 12410 days, 1768 weeks, and 408 months left.")

#1 year = 12 months

time_guage = 90
months_guage = int(time_guage) * 12
weeks_guage = int(time_guage) * 52
days_guage = int(time_guage) * 365

days_left = days_guage - (int(age) * 365)
weeks_left = weeks_guage - (int(age) * 52)
months_left = months_guage - (int(age) * 12) 

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
