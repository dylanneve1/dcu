class Human:

	def sayHello(self, name=None, age=None):

		if name is not None and age is None:
			print 'Hello ' + name
		elif name is not None and age is not None:
			print 'Hello ' + name + age
		else:
			print 'Hello'

obj = Human()

obj.sayHello()

obj.sayHello('Dylan ')

obj.sayHello('Dylan ', '15')
