class MyClass():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def print_first(self):
        print(self.first)

first = input('First number')
second = input('Second number')
test = MyClass(first, second)
test.print_first()

class Animal():
    def __init__(self):
        print("Animal created!")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

dog = Dog()

