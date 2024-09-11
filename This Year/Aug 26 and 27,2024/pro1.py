"""
Given an array of strings and an input from the given array written words that rhymes the most with the given word and if two world rhymes the most then return the word with the least character count

Input : N = 4
        arr[] = ['gender','blender','blunder','under']
        thunder

Output : under
"""

def rhyme(num:int,StringList:list,String:str)->str:
        res = ''
        count = 0
        for i in StringList:
                value = sync(i,String)
                if value > count  :
                        count = value 
                        res = i
                elif value == count :
                        if len(i) < len(res):
                                res = i
        return res
            
def sync(word,phase):
        count = 0
        min_length = min(len(word),len(phase))
        for i in range(1,min_length+1):
                if word[-i] == phase[-i]:
                        count += 1
                else :
                        return count
        return count

num = int(input())
StringList = list(input().split())
String = input()

print(rhyme(num,StringList,String))