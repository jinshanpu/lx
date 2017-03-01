print 'With else:'
for i in range(1, 5):
	print i
else:
	print 'The loop is over'

print 'With break in for:'


for i in range(1, 5):
	# if i == 5, the loop has been finished, so though break is executed, but else would be not executed.
	if i == 4:
		break
	print i
else:
	print 'The loop is over because break above'

