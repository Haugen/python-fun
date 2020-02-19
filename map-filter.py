def square(num):
    return num**2

nums = [1, 2, 3, 4, 5]

# print(list(map(square, nums)))

# Lambda
print(list(map(lambda num: num ** 2, nums)))

def check_even(num):
    return num % 2 == 0

even = list(filter(check_even, nums))
# print(even)


