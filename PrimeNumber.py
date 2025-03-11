import math, random 

#Return if an integer is a prime number or not 
def isPrimeDiv(val : int) -> bool :

    #1 and 0 are not prime number
    if val < 2 :
        return False
    
    for i in range(2, int(math.sqrt(val)) + 1) :
        if val%i==0 :
            return False

    return True

#Eratosthenes' Sieve
def primeSieve(size : int) :
    PrimeList = [True for i in range(size)]
    PrimeList[0] = False
    PrimeList[1] = False 

    for i in range(2, int(math.sqrt(size)) + 1) :
        if PrimeList[i]:  # Only sieve from prime numbers
            pointer = i * i
            while pointer < size:
                PrimeList[pointer] = False
                pointer += i  # Increment by i to mark all multiples of i
    
    primes = [i for i in range(size) if PrimeList[i]]
    
    return primes

def power_mod(base, exp, mod):
    """Computes (base^exp) % mod using modular exponentiation."""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1  # Integer division by 2
        base = (base * base) % mod
    return result

def rabin_miller(n, k=20):
    """Rabin-Miller primality test for n, k is the number of iterations."""
    if n <= 1:
        return False
    if n == 3:
        return True
    if n % 2 == 0:
        return False

    # Decompose n-1 into 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Repeat k times for better accuracy
    for _ in range(k):
        a = random.randint(2, n - 2)  # Choose random base a
        x = power_mod(a, d, n)
        
        if x == 1 or x == n - 1:
            continue  # If x == 1 or x == n-1, this base passes the test

        # Square and check if any power of x equals n-1
        for _ in range(r - 1):
            x = power_mod(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # If we never get x == n-1, n is composite

    return True  # If we pass all iterations, n is probably prime

#The goal is to have an efficient way to know if a large number is a 
#prime number or not so we can use the first prime number
#before using the rabin miller method
LOW_PRIME = primeSieve(100)

def isPrime(num : int) :
    if num<2 :
        return False
    
    for prime in LOW_PRIME :
        if num==prime :
            return True
        if num%prime==0 :
            return False
    
    #If we already don't know if the number is prime or not 
    #We use the rabin miller method
    return rabin_miller(num,100)


#Generate large prime number 
def generateLargePrimeNumber(keysize=1024) :
    while True :
        num = random.randrange(2**(keysize-1),2**keysize)
        if isPrime(num) :
            return num

