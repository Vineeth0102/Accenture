"""
Given an array with 'N' Elements you are expected to find the sum of the values that are present in the prime index of the array note that the array index starts with 0 i.e the position (index) on the array element is 0, the position os the next element is 1 and so on

input : N = 10, arr [] = [1,2,3,4,5,6,7,8,9,10]
output : 

"""

def isPrime(num:int)->bool:
    if num <2:
        return False
    for i in range(2,num-1):
        if num%i == 0:
            return False
    return True

def sumPrime(arr : list,n : int)-> int:
    sum = 0
    for i in range(2,n):
        if isPrime(i) :
            sum += arr[i]
    return sum

n = int(input())
arr  = list(map(int,input().split()))

print(sumPrime(arr,n))