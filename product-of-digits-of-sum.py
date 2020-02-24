# https://edabit.com/challenge/HrQoXJYqpYZ2Rqvtb
# Product of Digits of Sum

def sum_dig_prod(*argv):
  s = str(sum(argv))
  while len(s) > 1:
    new = 1
    for n in [int(i) for i in s]:
      new = new * n
    s = str(new)
  print(int(s))

sum_dig_prod(16, 28) # 6
sum_dig_prod(0) # 0
sum_dig_prod(1, 2, 3, 4, 5, 6) # 2