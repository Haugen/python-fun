def longest_substring(digits):
	prev = None
	curr = []
	subs = []

	for digit in digits:
		if int(digit) % 2 == 0:
			if prev == 'even':
				if len(curr) > 1: subs.append(curr)
				curr = []
			curr.append(digit)
			prev = 'even'
		if int(digit) % 2 == 1:
			if prev == 'odd':
				if len(curr) > 1: subs.append(curr)
				curr = []
			curr.append(digit)
			prev = 'odd'

	if len(curr) > 1: subs.append(curr)
	subsStr = list(map(lambda lst : "".join(lst), subs))
	return max(subsStr, key=len)

longest_substring("225424272163254474441338664823") # "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") # "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") # "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.