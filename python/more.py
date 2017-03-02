l = [2,3,4]
l2 = [2*i for i in l if i >1]
print l2


def powersum(power, *args):
	total = 0
	for i in args:
		total += pow(i, power)
	return total

print powersum(2,3,4,5)


def make_repeater(n):
	return lambda s: s*n

t = make_repeater(3)
print t('dsafafds')
print t(5)

assert t(5)>10

print repr(l2)
print `l2`
