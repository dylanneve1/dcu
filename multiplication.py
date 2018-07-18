# Imports. 
import time
import os
import sys

# Get number value.
number = int(input("Enter a number : "))
print(" ")
timez = 1

# Print the value's multiplication table.
# If number is over 100, display "Done".
while timez < 10:
	print(str(number * timez))
	timez += 1
	time.sleep(1)
else:
	print("\nDone.\n")
	# Restart script.
	python = sys.executable
	os.execl(python, python, *sys.argv)
