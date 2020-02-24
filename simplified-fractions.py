# https://edabit.com/challenge/vQgmyjcjMoMu9YGGW
# Simplified Fractions

def simplify(txt):
  n,d = map(int, txt.split('/'))
  result = ""
  
  while True:
    for i in reversed(range(2, int(n)+1)):
      if (d/i).is_integer() and (n/i).is_integer():
        n = n/i
        d = d/i
        break
    break

  if n > d and (n/d).is_integer():
    result = str(int(n/d))
  else:
    result = "/".join([str(int(n)),str(int(d))])

  print(result)


simplify("4/6") # "2/3"
simplify("10/11") # "10/11"
simplify("100/400") # "1/4"
simplify("8/4") # "2"