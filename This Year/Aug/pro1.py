"""
You are given four integers ABCD find some of the negative numbers out of these four numbers and print the same

Input : 2 -3 -14 7
Output : -17

"""

def NegativeSum(a:int,b:int,c:int,d:int)->int:
    count = 0
    if a < 0 : count += a
    if b < 0 : count += b
    if c < 0 : count += c
    if d < 0 : count += d
    return count

a,b,c,d = map(int,input().split())
print(NegativeSum(a,b,c,d))