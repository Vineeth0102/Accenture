"""
Given a string in input which is nothing but Words separated by a full stop and we have to return the largest size of the word
"""

def largestWord(arr:str)->str:
    words = arr.split(".")
    res = ''
    for word in words:
        if len(word) > len(res):
            res = word
    return res

String = input() 
print(largestWord(String))