"""
You are given a number N. If N is odd then print the value of the product of the digits of the number north otherwise print the value of the sum of the digits of the number N

Input format:
The input consists of a single line:
The line contains an integer i.e N
Input will be read from the STDIN By the candidate

Output format:
If N is odd then print the value of the product of the digits of the number otherwise print the value of the sum of the digits of the number

"""

def mul(num:int)->int:
    res = 1
    while num != 0:
        res *= num%10
        num //= 10
    return res

def add(num:int)->int:
    res = 0
    while num != 0:
        res += num%10
        num //= 10
    return res

def func(num:int)->int:
    if num%2 == 0:
        return mul(num=num)
    else :
        return add(num=num)
    
num = int(input())
print(func(num=num))