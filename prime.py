def primes(num):
    primes = [2]
    for x in range(3, num, 2):
        if is_prime(x):
            print(f'{x} is prime')
            primes.append(x)
    print(primes)
    return f'There are {len(primes)} primes in {num}'

def is_prime(num):
    for x in range(num + 1):
        if x == num:
            return True
        if x == 0 or x == 1:
            continue
        if num % x == 0:
            return False
    return False

print(primes(50))
