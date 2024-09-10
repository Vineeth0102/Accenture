"""
Googly Number

Googly prime number is defined as a number that is derived from the sum of its individual digits for example if N = 43 the sum of individual digits is 4 + 3 = 7 which is prime making it a googly number 4

Your task is to find whether the number is googly prime number or not

input : N = 123
ouput : False

input : N = 1235
ouput : True

"""

def isPrime(num:int)->bool:
    if num <2:
        return False
    for i in range(2,num-1):
        if num%i == 0:
            return False
    return True

def GooglyPrime(N:int)->bool:
    res = 0
    while N != 0 :
        res = res + N%10
        N = N//10
    return isPrime(res)


N = int(input())
print(GooglyPrime(N))