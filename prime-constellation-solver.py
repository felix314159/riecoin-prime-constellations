# pip install sympy
from sympy import isprime, prime

# isprime(int) returns true/false

def get_first_n_primes_as_list(n: int):
	return [prime(i) for i in range(1, n+1)]

# riecoin prime constellations (7-tuple patterns)
constellation1 = [2, 6, 8, 12, 18, 20]
constellation2 = [2, 8, 12, 14, 18, 20]

# smallest solution: p=11
def findConstellation1Solution():
	primeList = get_first_n_primes_as_list(5)
	for i in primeList:
		amountOfSuccessesWithinConst = 0
		for j in constellation1:
			if isprime(i+j):
				print(f"{i}+{j}={i+j} is prime")
				amountOfSuccessesWithinConst += 1
				if amountOfSuccessesWithinConst == len(constellation1):
					print(f"Found constellation1 solution for p={i}!")
					exit(0)
			else:
				amountOfSuccessesWithinConst = 0
				print()
				break # if not every value in resulting sequence is prime no need to continue with it

# smallest solution: p=5639
def findConstellation2Solution():
	primeList = get_first_n_primes_as_list(4500)
	for i in primeList:
		amountOfSuccessesWithinConst = 0
		for j in constellation2:
			if isprime(i+j):
				print(f"{i}+{j}={i+j} is prime")
				amountOfSuccessesWithinConst += 1
				if amountOfSuccessesWithinConst == len(constellation1):
					print(f"Found constellation2 solution for p={i}!")
					exit(0)
			else:
				amountOfSuccessesWithinConst = 0
				print()
				break # if not every value in resulting sequence is prime no need to continue with it

def main():
	findConstellation2Solution()


main()
# Purpose: Find example solution for the two prime constellations accepted as solution in Riecoin's Stella PoW
