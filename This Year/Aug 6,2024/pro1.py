"""
Find the first keywords of the string

input - str = " My name is Vineeth Shettigar ", k= 3
output "My anme is "
"""
def intialPrint(String:str,k:int)->str:
    str_list = String.split()
    return str_list[:k]
String = input()
k = int(input())

print(*intialPrint(String,k))