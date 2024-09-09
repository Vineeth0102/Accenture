n = int(input())
list1 = list(map(int,input().split()))

even_index = 0
odd_index = 0 
for i in range(len(list1)):
    if i %2 == 0 :
        even_index ^= list1[i]
    else :
        odd_index += list1[i]
print(odd_index-even_index)