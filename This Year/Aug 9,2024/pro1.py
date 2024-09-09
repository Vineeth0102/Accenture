"""
You are on a  hiking trail represented by an array A of length N where the trial initially ascends and then descends forming a single peak your task is to find and return an integer value representing the elevation of the summit

input - n= 7 ,arr = [1,2,3,4,3,2,1]
output - 4

input - n= 2 ,arr = [5,3]
output - 5

"""
def peak(N:int,arr:list)->int:
    i,j = 0,num-1 
    while(i<=j):
        mid = i + (j-i)//2
        if mid == 0 and arr[mid] > arr[mid+1]:
            return(arr[mid])
        elif mid == num-1 and arr[mid] > arr[mid-1]:
            return(arr[mid])
        elif arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return(arr[mid])
        elif arr[mid] < arr[mid+1]:
            i = mid+1
        else :
            j = mid -1

num = int(input())
arr = list(map(int,input().split()))
print(peak(num,arr))



