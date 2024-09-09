"""
Alice has a pair of magical shoes that allows her to climb three stars at once in a city there are N houses whose roof Alice wants to reach the number of ropes of each house is given in an array A alice can reach the roof of only the house where the number is multiple of three your task is to find and return integer value representing the count of the number of houses whose roof Alice can climbed

input N=4 arr[] = [12,16,21,20]
output - 2

"""
def countHouses(num:int,arr:list)->int:
    count = 0
    for i in arr:
        if i%3==0:
            count+=1
    return count

num = int(input())
arr = list(map(int,input().split()))
print(countHouses(num=num,arr=arr))
