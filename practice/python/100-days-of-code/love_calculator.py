print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

first_person = name1.lower()
second_person = name2.lower()

t = first_person.count('t')
r = first_person.count('r')
u = first_person.count('u')
e = first_person.count('e')
l = first_person.count('l')
o = first_person.count('o')
v = first_person.count('v')
e1 = first_person.count('e')

t1 = second_person.count('t')
r1 = second_person.count('r')
u1 = second_person.count('u')
e2 = second_person.count('e')
l1 = second_person.count('l')
o1 = second_person.count('o')
v1 = second_person.count("v")
e3 = second_person.count('e')

love_count  = t + r + u + e + t1 + r1 + u1 + e2

love_count1  = l + o + v + e1 + l1 + o1 + v1 + e3

score = int(str(love_count) + str(love_count1))

if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
        print(f"Your score is {score}, you are alright together.")
else:
        print(f"Your score is {score}.")
