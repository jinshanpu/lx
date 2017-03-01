name = "china"

if name.startswith('ch'):
	print 'Yes, it starts with "ch"'

if 'a' in name:
	print 'Yes, it contains the letter "a"'

if name.find("in"):
	print 'Yes, it contains the substring "in"'

delimiter = '_*_'
l = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(l)
