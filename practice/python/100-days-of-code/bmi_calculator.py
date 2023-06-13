# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / (height**2))

if BMI == 18.5:
       print("you are underweight.")
elif BMI <= 25:
       print("you have a normal weight")
elif BMI > 25 < 30:
       print("you are slightly overweight")
elif BMI > 30 < 35:
       print("you are obese")
elif BMI > 35:
       print("you are clinically obese")
