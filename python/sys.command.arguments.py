import sys

print 'The command line arguments are:'
count=0
for i in sys.argv:
	print 'sys.argv[', count ,']', i
	count+=1

print '\n\nThe PYTHONPATH is', sys.path, '\n'
