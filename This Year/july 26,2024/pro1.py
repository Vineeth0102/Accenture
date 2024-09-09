"""
Alex is given a Number N and wants you to rearrange the bits of the number in its binary representation such that all set bits are in consecutive order your task is to find and return an integer value representing the minimum possible number that can be formed after rearranging the bits of the number N

input - 10
output - 3


input - 2
output - 1
"""

num = int(input())
bin_num = bin(num).split("b")[1]
count = bin_num.count("1")

val = "1"* count
print(int(val,base=2))

# other approch

num = int(input())
bin_num = bin(num).split("b")[1]
count = bin_num.count("1")

print(2**count -1)