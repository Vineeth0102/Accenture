"""
You're working on a financial analysis tool which represents daily stock price of a company over time each element in an integer array a of size N represents the closing price of the stock for that particular day your task is to find and return an integer value representing the total number of days where the stock market price decreased indicating a negative growth

input - N = 6 , arr[] = [2,3,1,4,5,2]
output - 2

"""

def countDip(arr:list,num:int)->int:
    count = 0
    for i in range(N-1):
        if arr[i] > arr[i+1]:
            count+=1
    return count
N = int(input())
arr = list(map(int,input().split()))


print (countDip(arr=arr,num=N))