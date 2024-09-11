"""
Bob desires to buy N candies. The price of each candy is given in an array. Bob has M amount of money. The best deal for him in the supermarket is that if the price of the candy is multiple of five then he does not have to pay for the rest he has to pay the amount mentioned in the a[i] that is the exact amount

Input formt :
input1 : Number of candies N
input2 : Array of price of candies
input3 : Amount of money M

Output format:
Return the maximum number of candies that he can buy

"""

def candyCount(arr : int,money:int)->int:
    count = 0
    arr = sorted(arr)
    for i in arr :
        if i%5 == 0:
            count +=1
        elif i <= money :
            count +=1
            money -= i
    return count

num = int(input())
arr = list(map(int,input().split()))
money = int(input())

print(candyCount(arr,money))