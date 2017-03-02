class Person:
	'''Represents a person'''
	population = 0
	def __init__(self, name):
		self.name = name
		print '(Initializing %s)' % self.name
		Person.population += 1

	def __del__(self):
		print '%s says bye.' % self.name
		Person.population -= 1
		if Person.population == 0:
			print 'I am the last one.'
		else:
			print 'There are still %d people left.' % Person.population

	def sayHi(self):
		print "Hi, my name is %s" % self.name

	def howMany(self):
		if Person.population == 1:
			print 'I am the only person here.'
		else:
			print 'We have %d persons here.' % Person.population

jim = Person('Jim')
jim.sayHi()
jim.howMany()


tom = Person('Tom')
tom.sayHi()
tom.howMany()
del tom
'''
if no del here, you maybe be see a exception "Exception AttributeError: "'NoneType' object has no attribute 'population'" in <bound method Person.__del__ of <__main__.Person instance at 0x7f923a960830>> ignored"
because del will wait and go to the end
'''
