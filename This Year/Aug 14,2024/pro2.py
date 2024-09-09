"""
The function accepts an integer array'arr' Of size N as its argument.The function needs to return the index of an equilibrium point in an array where the sum of the elements on the left of the index is equal to the sum of the elements on the right of the index if no equilibrium point exists return -1


"""

def midSplit(arr:list)->int:
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            
            return i
    return -1

arr  = list(map(int,input().split()))
print(midSplit(arr=arr))

