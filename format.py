inp = str(input())
inp = inp.split("\n")
for pair in inp:
	pair = pair.split("\t")
	city = pair[1]
	country = pair[0]
	print(f'{"{country}","{city}"}')

