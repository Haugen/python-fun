from random import randint

x = randint(0,2)
result = input('Guess a number between 0 and 10\n')

if x == int(result):
    print('You guessed right!')
else:
    print('Wrong guess')
    print(f'The number was {x}')
