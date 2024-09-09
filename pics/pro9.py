n = int(input())
list1 = list(map(int,input().split()))

res = []

for i in range(len(list1)):
    for j in range(i,len(list1)):
        if list1[i] + list1[j] == 18 :
            res.append([list1[i] , list1[j]])
print(res)