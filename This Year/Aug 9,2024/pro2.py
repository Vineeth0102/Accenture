"""
You are given an integer N and a string as your task is to find and written new string which consists of the original string repeated N times 

input - N = 3 , str = "abc"
output - "abcabcabc" 

"""

def repeat(num:int,String:str)->str:
    return String*num

num = int(input())
String = input()
print(repeat(num,String))
