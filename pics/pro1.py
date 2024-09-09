"""
Island Life

You are stuck on an island where they sell and eat coconut sweets only. A person can buy at most 1 box per day with each box contening N preces. To remain alive, you must consume E coconut sweets daily for D days, but the catch is that you cannot purchase sweets on Sundays. Your task is to find and retum an integer valur representing the minimum number of times you have to buy coconut sweerts m order to stay alive. If not possibile, retu

Note: The day strom Monday

Input Specification:

Input: An integer value. N representing the number of coconut sweets per box

inputz : An integer value E. represetting the number of coconut sweets you must eat daily

input3: An integer value D. representing the number of days you have to spend on the island

Output Specification

Returh an imeger value representing the main rainber of times you

"""

import math 

coconut_sweet_in_each_box  = int(input("Enter the number of coconut Sweets in each box : "))
daily_consumption = int(input("Enter the number of coconut Sweets you need to eat dailty to survive : "))
days_to_spend = int(input("Enter the number of days you need to spend on the island : "))

lhs = coconut_sweet_in_each_box * (days_to_spend - (days_to_spend//7))
rhs = daily_consumption*days_to_spend
if  lhs >= rhs:

    print(math.ceil(rhs /coconut_sweet_in_each_box))
else :
    print(-1)