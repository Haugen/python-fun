list1 = ['one', 'two', 'three']
list2 = ['four', 'five']

list2.append('six')
list1 + list2 # Concatinate lists
list1.pop(2) # Pops at inde

newlist = [0, 1, 12,  2, 9, 3, 4, 8, 5, 22, 6, 7]
newlist.sort()
newlist.reverse()

# print(newlist)

# List comprehension
alist = [letter for letter in 'a word' if letter != ' ']
print(alist)

celcius = [0, 10, 20, 45.5]
fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)
