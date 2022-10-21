"""
Arrange primes in a string upto a certain number
"""

import math

def checkprime(n):
    if(n <= 1):
        return False
    if(n <= 3):
        return True
    if(n % 2 == 0 or n % 3 == 0):
        return False
    for i in range(5,int(math.sqrt(n)),6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
    return True
    
def nextprimenumber(n):
    if(n==1):
        return 2
    foundnext = False
    while(foundnext == False):
        n+=1
        if(checkprime(n) == True):
            foundnext = True
    return n
    
def fillprimestring(size):
    currentPrime = 2
    AllPrimeStrings = '2'
    while len(AllPrimeStrings) < size:
        nextPrime = nextprimenumber(currentPrime)
        AllPrimeStrings += str(nextPrime)
        currentPrime = nextPrime
    return AllPrimeStrings

def solution(i):
    ID = fillprimestring(10005)[i:i+5]