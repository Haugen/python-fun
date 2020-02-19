# name = input('Greet someone: \n')

def a_function(name='DEFAULT NAME'):
    print(f'Hello {name}')

def pig_latin(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    new_words = []
    for word in s.split():
        if word[0] in vowels:
            new_words.append(word + 'ay')
        else:
            new_word = word + word[0] + 'ay'
            new_word = new_word[1:]
            new_words.append(new_word)
    return ' '.join(new_words)

print(pig_latin('This is a string that we can use to practice with functions'))

def argsexample(*args):
    # args will be a tuple
    return sum(args) * 0.05

print(argsexample(10, 50, 3, 6, 2))

def kwargs(**kwargs):
    print(kwargs)

kwargs(fruit='apple',another='banana')

# Can be combined like
def combo(*args, **kwargs):
    pass
