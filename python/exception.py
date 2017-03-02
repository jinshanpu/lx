import sys

class ShortInputException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length= length
		self.atleast = atleast

try:
	s = raw_input('Enter sth -->')
	if len(s) < 3:
		raise ShortInputException(len(s), 3)

except EOFError:
	print '\nWhy did you give me a EOF?'
	sys.exit()
except ShortInputException, x:
	print 'ShortInputException: the input was of length %d, was expecting at least %d' % (x.length, x.atleast)
#except:
#	print 'What is wrong?'
else:
	print 'Hah, everything is good!'
finally:
	print 'I will always be here!'

print 'Done'
