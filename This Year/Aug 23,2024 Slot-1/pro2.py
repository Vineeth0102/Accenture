"""
Charles is given an array A. He wants to find the count of occurrences of the second largest element in the array Your task is to help him to find and return an integer value representing the count of occurrence of the second largest element in an array

Note :
If the array contains same element then return 0
The area has only consecutive elements that is in sorted order

Input : N = 5 arr[] = [1,2,3,3,4,4]
Output : 2
"""

def SecondCount(num :int,arr:int)->int:
    ref = arr[-1]
    count = 0
    for i in range(num-1,-1,-1):
        if arr[i] != arr[i-1] and ref == '':
            ref = arr[i-1]
        elif ref == arr[i]:
            count+=1
        elif ref != arr[i]:
            return count
        
num = int(input())
arr = list(map(int,input().split()))
print(SecondCount(num,arr))