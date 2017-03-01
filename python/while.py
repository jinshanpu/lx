number =23
running = True
while running:
	guess=int(raw_input('Enter an integer: '))
	if guess == number:
		print 'Good, you got it!'
		print 'But there is no prize'
		running=False
	elif guess < number:
		print 'it is higher than that'
	else:
		print 'it is lower than that'
