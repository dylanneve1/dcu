import time
import os
import sys

class binaryConverter:

	def main(self):

		print("\nConversion options :\n")
		print("1 - Number to binary.")
		print("2 - Binary to number.")
		print("3 - Add binary.")
		print("4 - Subtract binary.\n")
		mode = int(input("Selection : "))
		print("\n")

		if mode is 1:
			inputNumber = input("Enter number : ")
			print("\n" + bin(inputNumber))

		elif mode is 2:
			inputNumber = "0b" + str(input("Enter binary : "))
			finalValue = int(inputNumber, 2)
			print("\n" + str(finalValue))

		elif mode is 3:
			firstNumber = "0b" + str(input("Enter first number : "))
			secondNumber = "0b" + str(input("Enter second number : "))
			addedValues = (int(firstNumber, 2)) + (int(secondNumber, 2))
			print("\n" + bin(addedValues))

		elif mode is 4:
			firstNumber = "0b" + str(input("Enter first number : "))
			secondNumber = "0b" + str(input("Enter second number : "))
			subtractedValues = (int(firstNumber, 2)) - (int(secondNumber, 2))
			print(bin(subtractedValues))

		else:
			print("\nINVALID OPTION")
			exit()

b = binaryConverter()

b.main()

# Restart script.
python = sys.executable
os.execl(python, python, *sys.argv)
