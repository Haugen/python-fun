# https://edabit.com/challenge/Fpymv2HieqEd7ptAq
# Parentheses Clusters

def split(txt):
  balanced = []
  distance = 0
  index = 0

  for i in range(len(txt)):
    if txt[i] == "(":
      distance += 1
    if txt[i] == ")":
      if distance == 1:
        balanced.append(txt[index:i+1])
        index = i+1
        distance = 0
      else:
        distance -= 1

  print(balanced)


split("()()()") # ["()", "()", "()"]
split("((()))") # ["((()))"]
split("((()))(())()()(()())") # ["((()))", "(())", "()", "()", "(()())"]
split("((())())(()(()()))") # ["((())())", "(()(()()))"]