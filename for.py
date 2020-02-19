mylist = [1, 2, 3, 4, 5, 6]
for num in mylist:
    if num % 2 == 0:
        print(num)

tuplist = [(1,2),(3,4),(5,6),(7,8)]
for a,b in tuplist:
    pass

trip = [(1,2,3),(4,5,6)]
for a,b,c in trip:
    pass

d = {'k1': 1, 'k2': 2, 'k3': 3}
for key,value in d.items():
   print(key)
   print(value)

for index,letter in enumerate('Tobias'):
    pass

list1 = [1,2,3]
list2 = ['a','b','c']
# Can zip with more than two list
zippedlist = zip(list1,list2)
for item in zip(list1, list2):
    print(item)

