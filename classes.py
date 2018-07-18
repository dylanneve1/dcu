class Talk:
	
	def speak(self, name=None, age=None):
	#def speak(self, name, age=None):
		
		if name is None and age is None:
			print("Hello")
		elif name is None and age is not None:
			print("Hello person who is " + age)
		elif name is not None and age is None:
			print("Hello " + name)
		elif name is not None and age is not None:
			print("Hello " + name + " who is " + age)

t = Talk()

t.speak('Dylan')
t.speak(None, '15')
t.speak()

print("\n\n")

inputedName = str(input("What is your name? "))
inputedAge = str(input("What is your age? "))

t.speak(inputedName, inputedAge)
