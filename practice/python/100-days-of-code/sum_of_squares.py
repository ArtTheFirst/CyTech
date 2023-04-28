rnd_digits = input("Input a list of digits ").split()

ans_slot = 0
for alldigit in rnd_digits:
    ans_slot += int(alldigit)** 2
print(ans_slot)
