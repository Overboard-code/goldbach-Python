# Goldbach's Conjecture tester for all even numbers up to N. 
import sys
from gmpy2 import is_prime
# or use home grown IsPrime
sys.set_int_max_str_digits(20000)

def IsPrime(n):  
	if (n <= 1):  
		return False      
	if (n <= 3):  
		return True        
	if (n%2 == 0 or n%3 == 0):  
		return False      
	for i in range(5,int(n**.5)+1): 
		if (n%i == 0 or n%(i+2) == 0):  
			return False          
	return True  

def goldbach(number):    
    if number == 4:
        return 2,2
    elif is_prime(number - 3):
        return 3,number-3
    else:
        for p in range(5, number, 6): # just check 6k±1 
            if is_prime(p ) and is_prime(number-p ): 
                return p,number-p
            elif is_prime(p+2) and is_prime(number-(p+2) ):
                return p+2,number-p+2
        return 0,0

def check(N):
    for n in range(4,N+1,2):
        g = goldbach(n)
        if g == (0,0):
            print("No sum found for %d !" % n)
            raise Exception(f"Found a counter-example to the Goldbach conjecture: {n}")
        else:
            print("%d is equal to %d + %d" % (n, g[0], g[1]))
    return

if __name__=="__main__":
    N = 0
    args = len(sys.argv)
    if args > 1:
        N = int(sys.argv[1])
    print("This is a test of Goldbach's Conjecture that for all even integers")
    print("greater than 2 there are two primes that add up to that even number.\n")
    
    while (N < 3):
        N = int(input("Please enter a number > 3 to check all evens to N> "))
    print("All even numbers up to %d will be tested" % N) 
    check(N)