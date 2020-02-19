# https://edabit.com/challenge/4AjWvJdZpFEMbGALd
# Josephus Permutation

def who_goes_free(n, k):
  lst = list(range(0,n))

  start = k
  while len(lst) > 1:
    for item in lst:
      indexes = list(range(start - 1, len(lst), k))
      lastIndex = indexes[-1]
      start = k - (len(lst) - 1 - lastIndex)
      for i,remove in enumerate(indexes):
        lst.pop(remove - i)
      while start > len(lst):
        start = start - len(lst)
  print(lst[0])

who_goes_free(9, 2) # 2

# Prisoners = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Executed people replaced by - (a dash) for illustration purposes.
# 1st round of execution = [0, -, 2, -, 4, -, 6, -, 8]  -> [0, 2, 4, 6, 8]
# 2nd round = [-, 2, -, 6, -] -> [2, 6]  # 0 is killed in this round because it's beside 8 who was skipped over.
# 3rd round = [2, -]

who_goes_free(9, 3) # 0

# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, -, 3, 4, -, 6, 7, -] -> [0, 1, 3, 4, 6, 7]
# [0, 1, -, 4, 6, -] -> [0, 1, 4, 6]
# [0, 1, -, 6] -> [0, 1, 6]
# [0, -, 6] -> [0, 6]
# [0, -] -> [0]

who_goes_free(7, 3) # 3
who_goes_free(53, 7) # 21