from sys import argv

print 'The command line arguments are:'
count=0
for i in argv:
	print 'argv[', count ,']', i
	count+=1

print 'My module name is ',__name__
