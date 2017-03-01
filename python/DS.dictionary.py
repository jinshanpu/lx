ab={
	'Zack'	:	'zack@hotmail.com',
	'Larry' :	'l@gmail.com',
	'Jim'	:	'sadf.jim@gmail.com'
}

print 'Jim\' address is %s' % ab['Jim']

ab['Jim'] = 'new.jim@gmail.com'
del ab['Zack']

for name, address in ab.items():
	print '%s ==> %s' % (name, address)

if 'Lilei' in ab:
#or if ab.has_key('Lilei'):
	print 'Yes!'

