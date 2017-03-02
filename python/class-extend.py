class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print '(initialized school member: %s' % self.name
	
	def tell(self):
		print 'Name: %s, age: %d' % (self.name, self.age)

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print '(Initialized Teacher: %s)' % self.name
	
	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: %d' % self.salary

class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print 'Initialized Studuents: %s' % self.name
	def tell(self):
		SchoolMember.tell(self)
		print 'Marks: %d' % self.marks

t = Teacher('Mrs. Simith', 40, 300000)
s = Student('LiLei', 22, 99)

print

members = [t, s]
for member in members:
	member.tell()
