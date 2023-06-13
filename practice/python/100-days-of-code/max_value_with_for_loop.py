student_scores = input("Input a list of student scores ").split()
#for n in range(0, len(student_scores)):
    
 #print(student_scores)

max_value = 0
for height_values in student_scores:
    if height_values > max_value:
        max_value = height_values

print(f"The highest score in the class is: {max_value}")
