"""
Count minimum right flips to set all values in an array

N light bulbs are connected by a wire each bulb has a switch associated with it however due to a faulty buyer is with also changes the state of all the bulbs to the right of the current bulb given an initial state of all bulbs find the minimum number of switches you have to press to turn on all the bulbs you can press the same switch multiple times 

Note : Zero represents the bulb is off and one represents the bulb is on

input arr[] = [0,1,0,1]
ouput - 4

"""

def minSwitch(arr:list)->int:
    count = 0
    for i in range(len(arr)-1,-1,-1):
        if i == 0 :
            count+=1
        elif arr[i] != arr[i-1]:
            count+=1
    return count


arr = list(map(int,input().split()))
print(minSwitch(arr))