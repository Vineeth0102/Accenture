"""
Convert a number N into its binary form (String)

Input : N = 10
Output : 1010

Input : N = 3
Output : 11

"""

def Binary(num:int)->str:
    binNumber = bin(num)
    binNumber = binNumber.split('b')[1]
    return binNumber


num = int(input())
print(Binary(num=num))