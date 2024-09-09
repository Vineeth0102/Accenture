"""

Repeat String

You are given an integer N and a string S. Your task is to find and return a new string which consists of the original string repeated N times.

Input Specification:

input1: An integer value N

input2: A string value S

Output Specification:

Return a new string which consists of the original string repeated N times.

36151

Example 1:

input1: 3

input2: abc

9047

Output: abcabcabc
"""

num = int(input("Enter the number of time it has to be repeated : "))
String =  input("Enter the String : ")

print(String*num)