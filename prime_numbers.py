lower = int(input("Enter lower end of range :"))
upper = int(input("Enter upper end of range :"))
primes = []

print("\nChecking for prime numbers between " + str(lower) + " and " + str(upper) + "\n\n")

for num in range(lower, upper, + 1):
	for i in range(2, num):
		if(num % i) == 0:
			print(str(num) + " is not a prime number"

