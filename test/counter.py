# Imports. 
import time
import os
import sys

# Get counter value.
counter = int(input("Enter a number : "))
print(" ")

# Print the value of counter going down by one every second. 
# If counter is at 0, display "Done".
while counter >= 0:
	print(str(counter))
	counter -= 1
	time.sleep(1)
else:
	print("\nDone.\n")
	# Restart script.
	python = sys.executable
	os.execl(python, python, *sys.argv)
