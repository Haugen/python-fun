def longest_zero(s):
  temp = []
  z = []

  for i,l in enumerate(s):
    if l == "0":
      temp.append(l)
      if len(s) == i + 1 and len(temp) > len(z):
        z = temp
    else:
      if len(temp) > len(z): z = temp
      temp = []
              
  print("".join(z))

longest_zero("01100001011000") # "0000"
longest_zero("100100100") # "00"
longest_zero("11111") # ""
longest_zero("100001110000100000") # "00000"