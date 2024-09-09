"""
You are given a string S and your task is to find and return the count of permutation performed by fixing the position of vowels present in the string

Note :
- Ensure the result is non-negative
- If there are no consonants then return 0

"""

def PermuationCount(String :str)->int:
    String = String.lower()
    res,val = 1,1
    for i in String :
        if not (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ):
            res *= val
            val+=1
    return res 

String = input()
print(PermuationCount(String=String))