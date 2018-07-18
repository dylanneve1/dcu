class Pen:

	def __call__(self, penHadLid=None, penColour=None):
		self.__printOnScreen__(penHasLid, penColour)

	def __printOnScreen__(self, shownLidPos=None, shownColour=None):
		if shownLidPos is False and shownColour is "red":
			print("You have a red pen with a lid")

p = Pen()

userChosenLidOrNot = str(input("\nDoes pen have a lid? True/False : "))
userChosenColour = str(input("What colour is the pen? red/green/blue : "))

p(userChosenLidOrNot, userChosenColour)
