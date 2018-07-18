import time

class binaryConverter:

	def main(self):

		print("\nConversion options :\n")
		print("1 - Number to binary.")
		print("2 - Binary to number.\n")
		mode = int(input("Selection : "))
		print("\n\n")

		if mode is 1:
			inputNumber = input("Enter number : ")
			print("\n\n")
			print(bin(inputNumber))

		elif mode is 2:
			inputNumber = input("Enter binary : ")
			print("\n\n")
			convertedValue = str(inputNumber)
			print(convertedValue)

		else:
			exit()

b = binaryConverter()

b.main()
