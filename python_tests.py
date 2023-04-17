
 #Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(0, nr_letters + 1)
 

#student_scores = input("enter student scores: ").split()
#for score in student_scores:
 #student_scores += student_scores
#print (max(student_scores))

#student_heights = input("put list here ").split()
#for n in range(0, len(student_heights)):
 #student_heights[n] = int(student_heights[n])
#print(student_heights)

#total_height = 0
#for height in student_heights:
 #total_height += height
#print(total_height)

#number_of_students = 0
#highest_value = 0
#for student in student_heights:
 #if student > highest_value:
   #highest_value = student
#print(f"highest value is {highest_value}")
 #number_of_students += 1
#print(max(number_of_students))

#to add from 1 to 100, flip the pair and add each line
#i.e. 1+100, 2+99, 3+98 etc... there are 50 pairs. 
#multiply 101 by 50


#this function prints addition of even numbers from 1-100
#total = 0
#for number in range(2, 101, 2):
 #total += number
 #if number % 2 ==0
  #total +=number
#print(total)
#range functions in python = 
#(start, end, increment value)
#e.g 0, 1 increase by 3


#fizzbuzz program
#for number in range(1, 101):
 #if number % 3 ==0 and number % 5 == 0:
  #print(f"{number} fizzbuzz")
 #elif number % 3 == 0:
  #print(f"{number} fizz")
 #elif number % 5 == 0:
  #print(f"{number} buzz")
 #else:
  #print(number)
  
#/n is used for going to the next line in input 
#statements
 
#hang man program

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list) 

guess = input("guess a letter: ").lower()

for letter in chosen_word:
 if letter == guess:
  print("yea cool")
 else:
  print("nah do it again")