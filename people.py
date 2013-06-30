class Person(object):
	
	def __init__(self):
		self.givenname	= ''
		self.surname 	= ''

	def __str__(self):
		return "Person: " + self.fullname()

	def fullname(self):
		return self.givenname + ' ' + self.surname

	def lastfirst(self):
		return self.surname + ', ' + self.givenname



class Employee(Person):

	def __init__(self):
		self.id			= 0
		self.title 		= ''
		self.manager	= None
		self.extension	= ''

	def __str__(self):
		return "Employee: %s (%s) " % ( self.fullname(), self.title )


class Manager(Employee):

	def __init__(self):
		self.reports = []

	def __str__(self):
		return "Manager: %s (%s) %d reports" % ( self.fullname(), self.title, len(self.reports) )


