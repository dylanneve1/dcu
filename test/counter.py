# Imports. 
import time

# Get counter value.
counter = int(input("Enter a number : "))
print(" ")

# Print the value of counter going down by one every second.
# If counter is at 0, display "Done".
while counter >= 0:
	print(str(counter))
	counter = counter - 1
	time.sleep(1)
else:
	print("\nDone.")
