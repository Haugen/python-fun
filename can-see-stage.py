# https://edabit.com/challenge/xbjDMxzpFcsAWKp97
# Concert Seats

def can_see_stage(seats):
  for row in range(len(seats)-1):
    for seat in range(len(seats[0])):
      if seats[row][seat] >= seats[row+1][seat]: return False
  return True

can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) # True

can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) # True

can_see_stage([
  [2, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) # False

can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) # False

# Number must be strictly smaller than
# the number directly behind it.