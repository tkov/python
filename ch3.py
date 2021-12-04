"""
Dictionary and sets
"""

DIAL_CODES = [
		(86, 'China'),
		(91, 'India'),
		(1, 'US'),
		(62, 'Indonesia'),
		(55, 'Brazil'),
		(92, 'Pakistan'),
		(7, 'Russian'),
		(81, 'Japan'),
	]


# dict comprehensions...
country_code = {country: code for code, country in DIAL_CODES}

"""
Handling missing keys with 'setdefault'
"""

# d.get(k, default) is an alternative to d[k]

import sys
import re

WORD_RE = re.compile('\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
	for line_no, line in enumerate(fp, 1):
		for match in WORD_RE.finditer(line):
			word = match.group()
			column_no = match.start() + 1
			location = (line_no, column_no)
			index.setdefault(word, []).append(location)
			# this is ugly
			# occurances = index.get(word, [])
			# occurances.append(location)
			# index[word] = occurances


for word in sorted(index, key=str.upper):
	print(word, index[word])


"""
Sets
"""

# empty set is created using set() ({} is simply an empty dictionary)

s = {1}   # a set with one element
type(s)
s
s.pop()
s

frozenset(range(10))

# s.add() adds an element to a set s
# s.update() adds elements in a container (tuples, sets, lists, frozen-sets )
# s.add() adds tuples or frozensets themselves

a = set()
a.add(1)
a.add(2)

a.update([3,4])  # => {1,2,3,4}
a.add((5,6))	 # => {1,2,3,4, (5,6)}
