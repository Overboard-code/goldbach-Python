# Goldbach's Conjecture tester using Miller-Rabin primality test. 
import sys
import cProfile
import secrets
from gmpy2 import powmod
#from gmpy2 import is_prime
# or use home grown IsPrime
sys.set_int_max_str_digits(20000)
def millerTest(d, n):    
    a = 2 + secrets.randbelow(n - 4);
    x = powmod(a, d, n);
    if (x == 1 or x == n - 1):
        return True;
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
    return False;
 
def IsPrime( n ):
    k = min(int(len(str(n))/5) + 4,14)
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n&1==0):
        return False
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
    for i in range(k):
        if(millerTest(d, n) == False):
            return False
    return True

def goldbach(number):    
    if number == 4:
        print("\n2 + 2 = 4\n")
        return
    elif IsPrime(number - 3 ):
        print(f"\n3 + {number-3:,} = {number}\n")
        return
    else:
        for p in range(5, number, 6): # just 6k±1 
            if IsPrime(p ) and IsPrime(number-p ): 
                print(f"\n{p:,} + {number-p:,} = {number:,}\n")
                return
            elif IsPrime(p+2) and IsPrime(number-(p+2) ):
                print(f"\n{p+2:,} + {number-(p+2):,} = {number:,}\n")
                return
        raise Exception(f"Found a counter-example to the Goldbach conjecture: {number}")

if __name__=="__main__":
    import sys
    N = 1
    args = len(sys.argv)
    if args > 1:
            N = int(sys.argv[1])
    if IsPrime(N): 
        print(f"It's a Prime {N:,}")
        sys.exit(0)
    print("This is a test of Goldbach's Conjecture that for all even integers")
    print("greater than 2 there are two primes that add up to that even number.\n")
    while (N < 3 or N%2):
            N = int(input("Please enter an even number > 3 to check with Goldbach's Conjecture> "))
#goldbach(N)
    cProfile.run('goldbach(N)')
