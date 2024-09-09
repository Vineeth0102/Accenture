"""
Find count of a magical numbers from one to N

A number is magical if:
    ->Convert to Binary
    ->Replace 0 with 1 and 1 with 2 in the binary string
    ->Calculate sum of all digits in the binary string
    ->The resultant must be an odd number

input : N = 5
output : 2

"""
def magicCount(num:int)->int:
    count = 0
    for i in range(1,num+1):
        bin_number = bin(i).split('b')[1]
        if (bin_number.count("0")% 2)==1 :
            count+=1
    return count


num = int(input())
print(magicCount(num))

