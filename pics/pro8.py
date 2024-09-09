list1 = list(map(int,input().split()))
d = int(input())
q = int(input())
r = int(input())
n = int(input())

if d*q+r in list1:
    print(list1.index(d*q+r))
else:
    print(-1)