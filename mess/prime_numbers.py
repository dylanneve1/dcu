lower = int(input("\nEnter lower end of range :"))
upper = int(input("Enter upper end of range :"))
primes = []

print("\nChecking for prime numbers between",lower,"and",upper, end = "\n\n")

for num in range(lower, upper, + 1):
	for i in range(2, num):
		if(num % i) == 0:
			print(str(num) + " is not a prime number")
			break
	else:
		print(str(num) + " is a prime number")
		primes.append(num)

if(len(primes) > 0):
	print("\nThe set of prime numbers in that range is :",primes,"\n")
else:
	print("\nThere are no prime numbers in that range\n")
