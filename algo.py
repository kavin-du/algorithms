finding closest prime for a given number

from math import sqrt

def isPrime(n):
    if n==1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    else:
        return True

def closestPrime(n):
    if n%2 == 0:
        n -= 1
    while(True):
        if n%5 == 0:
            n -= 2
        if isPrime(n):
            return n
        else:
            n-=2

####################################################
# find Nth prime using sieve of irtothenisis

from math import log
import sys
def sievePrimes(n):
    if n==1:
        return 2
    k = int( n*log(n) + n*log(log(n)) )
    
    if n < 6:
        k+=3
    primes =[True]*(k+1)

    p = 2
    while(p*p < k):
        if primes[p]:
            for i in range(p*p, k+1, p):
                primes[i] = False
        p += 1
    j = 0
    for i in range(2, k+1):
        if primes[i] == True:
            j += 1
            if j == n:
                return i


#######################################

#list of first n primes

def sievePrimes(n):
    primes = [True]*(n+1)
    p = 2
    while(p*p < n):
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p+=1
    arr =[]
    for i in range(2, n+1):
        if primes[i]:
            arr.append(i)
    return arr

#########################################
#gcd of given two numbers euclidean

def gcd(a, b):
    if a < b:
        a, b = b,a
    if b == 0:
        return a
    return gcd(b, a%b)

