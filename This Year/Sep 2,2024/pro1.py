"""
Special Fibonacci sequence:
 
You are given a special fibonacci sequence defined by the following recurrence relation:
f(N) = f(N-1)*f(N-1) + f(N-2) * f(N-2)
With initial condition:
f(0) = 0
f(1) = 1

Input format:
The first and only line contains a singular integer
N(where N>=0)

Output format:
Print nth term of the special Fibonacci sequence modulo 47

"""


def specialFibb(n:int)->int:
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else :
        return specialFibb(n-1)**2 + specialFibb(n-2)**2 
    
num = int(input())
print(specialFibb(n=num+1)%47)