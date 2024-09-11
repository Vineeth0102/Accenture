"""
You are given an array arr Of length N . Find and print the element at the mid index of the array ignore all the indices at which the negative numbers are present in an array

Note :
In any case there are two midindegers print the element at the smaller index
You may assume that there will be at least one positive number in an array

Input  :
6
12 -3 14 -56 77 13

Output :
14
"""

def median(num : int,arr:list)->int:
    new_arr = []
    for i in arr :
        if i  > -1 :
            new_arr.append(i)

    mid = (len(new_arr) - 1) // 2
    return new_arr[mid]

num = int(input())
arr = list(map(int,input().split()))
print(median(num,arr))