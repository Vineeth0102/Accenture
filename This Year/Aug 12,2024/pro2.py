"""
find sum of all prime numbers till N

input N=8
output 17


"""

def isPrime(num:int)->bool:
    if num <2:
        return False
    for i in range(2,num-1):
        if num%i == 0:
            return False
    return True

def primeSum(num:int)-> int:
    count = 0
    for i in range(2,num+1):
        if isPrime(i):
            count+=i
    return count

num = int(input())
print(primeSum(num))