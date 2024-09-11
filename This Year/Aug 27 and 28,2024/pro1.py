"""
Calculate the spaces of two given input string and return a string with whether their difference is odd or even and count

"""

def count(str1 :str,str2:str)->str:
    count = abs(str1.count(" ") - str2.count(" "))
    if count %2 == 0:
        return f"Even:{count}"
    else :
        return f"Odd:{count}"
    pass

str1 = input()
str2 = input()
print(count(str1=str1,str2=str2))