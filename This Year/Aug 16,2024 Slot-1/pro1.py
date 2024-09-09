"""
Jack has an array A of length N. He wants to label whether the number in the array is even or odd. Your task is to help him and find and written a string with the labels even or odd in a sequence according to which the numbers appear in the array

input: N = 5 arr[] = [1,2,3,4,5]

"""

def EvenOdd(arr:list)->str :
    res = ""
    for i in arr:
        if i % 2 == 0:
            res += "Even"
        else :
            res += "Odd"
    return res

n = int(input())
arr  = list(map(int,input().split()))

print(EvenOdd(arr=arr))
