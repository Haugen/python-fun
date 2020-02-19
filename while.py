from random import shuffle, randint

x = 0

while x < 5:
    if x == 3:
        x += 1
        continue
    print(f'x is {x}')
    x += 1
else:
    print('x is now greater than 5')

# Range
for num  in range(1,10,2):
    print(num)

listfromrange = list(range(10))
# print(listfromrange)

shuffle(listfromrange)
print(listfromrange)
print(randint(0,100))
