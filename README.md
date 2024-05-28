# goldbach-Python
I was looking into various Goldbach conjecture tests in Python. I saw some people posting problems with numbers larger than 100 thousand taking a long while.

Usually what we see are a calculation of a range of prime numbers. either a Sieve is used or a modulus division looking for a number x%n==0 testing for a even factor. Any factor means N isn’t a prime. Then loop through all the numbers from 2 to the Number we are searching for.

I wrote a three line Goldbach tester:
```
  from sympy import isprime as p
  N=int(input())
  print(*[(i,N-i)for i in range(2,N-1)if p(i)&p(N-i)])
```
The output looks like:
```
python goldbach_little.py
124
(11, 113) (17, 107) (23, 101) (41, 83) (53, 71) (71, 53) (83, 41) (101, 23) (107, 17) (113, 11)
```
I decided I could do better if I checked just 6k±1 numbers for prime. I also realized to test Goldbach's Conjecture, one success was enough. The result would be fewer checks for prime.  


The result looks like:
```
def goldbach(number):  
    if number == 4:
        return 2,2
    elif isprime(number - 3):
        return 3,number-3
    else:
        for p in range(5, number, 6): # just 6k±1 
            if isprime(p) and isprime(number-p): 
                return p,number-p
            elif isprime(p+2) and isprime(number-(p+2) ):
                return p+2,number-p+2
        return 0,0
```
