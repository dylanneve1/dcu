import time

counter = int(input("Enter a number : "))

while counter >= 0:
	print(str(counter))
	counter = counter - 1
	time.sleep(1)
else:
	print("Done.")
