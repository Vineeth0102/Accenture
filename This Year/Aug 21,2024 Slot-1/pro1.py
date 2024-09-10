"""
Genarate Fibonacci series of a number

Input : N = 1
Output : 1

Input : N = 0
Output : 0

"""

def fibbo(num:int)->int:
    num1,num2 = 0,1
    if num < 0 :
        return -1
    if num == 0 :
        return 0 
    if num == 1:
        return 1
    for i in range(2,num+2):
        num1,num2 = num2+num1,num1
    return num1

num = int(input())
print(fibbo(num))