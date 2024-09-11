"""
Toss and score

You are playing a game of toys and score in a Hillwood City Mall with your friends the game consists of following rules:
Toss an unbiased coin multiple times
For each heads you get two points and each tail you lose 1 point
The game ends as soon as you get three heads in a row or You tossed the coin throughout the length of string S

You have been given a string as consisting of letter H for heads and T for tails sequence of result your task is to find and results you get on tossing end times integer value representing the final score you get once the game ends

"""

def Toss(num : int , Coin : int)->int:
    count = 0
    res = 0
    for i in Coin:
        if i == 'T':
            res -= 1
            count = 0
        elif i == 'H':
            res += 2
            count +=1
        if count == 3:
            return res
    return res

num = int(input())
Coin = list(input().split())
print(Toss(num,Coin))