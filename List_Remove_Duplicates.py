'''def unique(a):
	myset = set(a)
	return myset
a = [2, 4, 5, 6, 7, 7, 8, 10, 38, 23, 23, 8, 2]
print(unique(a))'''

def remove(a):
	add = []

	for i in a:
	    if i not in add:
	        add.append(i)
	return add
a = [1, 2, 2, 3, 4, 4, 5,6,6]
print(remove(a))

