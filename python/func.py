print "the prog knows which number is bigger"
a=int(raw_input("Number a:"))
b=int(raw_input("Number b:"))

def theMax(a, b=0):
	'''Prints the maximun of two numbers.
the two values must be integers'''
	if a>b:
		return a
	else:
		return b

print theMax(a, b)
print theMax.__doc__
