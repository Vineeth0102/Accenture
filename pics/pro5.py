list1 = list(map(int,input().split()))
n = int(input())

res = 0


if n%2 == 0 :
    for i in range(1,len(list1),2):
        res+= list1[i]
else:
    for i in range(0,len(list1),2):
        res+= list1[i]


print(res)
