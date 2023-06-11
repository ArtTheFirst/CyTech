num_lim = int(input("enter range of numbers to print: "))

def is_prime(num):
    if num < 2:
    #Zero and negative numbers are not prime
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes

print(generate_primes(num_lim))
