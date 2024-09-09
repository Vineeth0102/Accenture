"""
Alice has collection of songs represented as a string S where each character represents a song a playlist is substring of the given string with exactly K of songs she wants to create a playlist that contains maximum number of her favourite song which is "a" .Your task is to find and return an integer value representing the maximum number of favourite songs that she can listen and get it in a single playlist

input : s = 'acdbaaca' k=3
output : 2


"""

def playlist(String : str , k : int)->int:
    i,j,max_val = 0,0,0
    while j <=len(String):
        if j-i >= k:
            max_val = max(String[i:j].count('a'),max_val)
            i+=1
        j+=1
    return max_val

String = input()
k = int(input())

print(playlist(String=String,k=k))