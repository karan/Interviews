#!/usr/bin/python

'''
@author: Karan Goel
@email: karanmatic@gmail.com
'''

def combinations(a, b):
	'''
	Returns a collection of all the combinations of the 
	elements from two input lists.
	Params:
	\t`a`: a list of any size elements
	\t`b`: a list of any size elements
	Returns:
	\t`combs`: a list of tuples
	'''
	combs = []
	for elem_a in a:
		for elem_b in b:
			combs.append((elem_a, elem_b))
	return combs

def combinations_advanced(*args):
	'''
	Returns a collection of all the combinations of the 
	elements from any number of lists.
	Returns:
	\t`combs`: a list of tuples
	'''
	tuples = map(tuple, args) # comverts all lists into tuples
	combs = [[]] # holds list of lists, will be cast to list of tuples later
	for tup in tuples:
		# here, we take an already made "pattern", and add an element to it
		combs = [pat + [elem] for pat in combs for elem in tup]
	return map(tuple, combs) # cast list of list to list of tuples



a = ['a', 'b', 'c']
b = [1, 2]
c = []
d = [9, 8, 7, 6]

# prints [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]
print combinations(a, b)

# prints [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]
print combinations(b, a)

# print []
print combinations(c, a)

print '-' * 10

# prints [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]
print combinations_advanced(a, b)

# prints [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]
print combinations_advanced(b, a)

# print []
print combinations_advanced(c, a)

# prints a lot of things
print combinations_advanced(a, b, d)