total_round = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_round += i
print(total_round)

#it is important to make the last number 101, else 100 will not be counted
