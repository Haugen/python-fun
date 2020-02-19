def who_goes_free(n, k):
	while len(n) > 1:
		

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