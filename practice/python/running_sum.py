n_result = 0
n_digit = input("enter numbers: ").split()
for n in n_digit:
    if int(n) > 0:
        n_result += int(n)
        print(n_result)
    else:
        print(n_result)
