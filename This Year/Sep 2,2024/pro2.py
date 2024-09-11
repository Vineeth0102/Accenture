"""
Array index operation:

You are given an array of integer your task is to perform two operation:

Calculate the sum of the values at even indices in the array

Calculate the xor of the values at odd indices in the array

Finally return the sum of the results from the above two operations

"""

n = int(input())
list1 = list(map(int,input().split()))

even_index = 0
odd_index = 0 
for i in range(len(list1)):
    if i %2 == 0 :
        even_index+= list1[i]
    else :
        odd_index ^= list1[i]
print(odd_index+even_index)