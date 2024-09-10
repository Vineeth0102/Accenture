"""
Given a string and a two characters C1 and C2 as input, replace all the occurrences of Ch with C2 and C2 with C1 in the input string

Input : Ch = 'vineeth' ch = 'v' ch2 = 'e'
Output : einvvth
"""

def change(String:str,ch1:str,ch2:str)->str:
    for i in range(len(String)):
        if String[i] == ch1:
            String = String[:i] + ch2 + String[i+1:]
        elif String[i] == ch2:
            String = String[:i] + ch1 + String[i+1:]
    return String

String = input()
ch1 = input()
ch2 = input()

print(change(String,ch1,ch2))
