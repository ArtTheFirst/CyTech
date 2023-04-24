student_heights = input("Input a list of student heights ").split()
#for n in range(0, len(student_heights)):
  #student_heights[n] = int(student_heights[n])
  
height_sum = 0
for all_height in student_heights:
    height_sum += int(all_height)
          #print(height_sum)

heights_count = 0
for height_average in student_heights:
    heights_count += 1
          #print(heights_count)
print(round(height_sum / heights_count))
