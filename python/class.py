class Person:
	def __init__(self, name):
		self.name = name
	
	def sayHi(self):
		print "Hello, Good afternoon everyone, my name is " + self.name

p = Person("Tom")
p.sayHi()
