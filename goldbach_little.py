import cProfile,sys
#from sympy import isprime as IsPrime

def IsPrime( n ):
    from secrets import randbelow
    k = 6
    if (n <= 3): return n > 1
    if n%6 not in [1,5]: return False
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
    for i in range(k):
        x = pow(2 + randbelow(n - 4), d, n)
        if (x == 1 or x == n - 1): continue
        while (d != n - 1):
           x = (x * x) % n
           d *= 2;
           if (x == 1): return False
           if (x == n - 1): break
        else: return False
    return True        

def goldbach(number):
  if not number&1 and number > 3: # if even OK
    if number == 4: return 2,2
    elif IsPrime(number-3): return 3,number-3
    else: # just 6k±1
      for p,q in ((i,i+2) for i in range(5,number//2+1,6)): 
         if IsPrime(number-p) and IsPrime(p): 
            return p,number-p
         if IsPrime(number-q) and IsPrime(q): 
            return q,number-q
  return None # failed, all odds fail

	

a = 2**100
if len(sys.argv) > 1:
    a = int(sys.argv[1])
cProfile.run('print(goldbach(a))')