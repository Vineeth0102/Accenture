"""
You are developing a feature for an environmental awareness app that helps users to know how much area their trees shadow cover you have the distance D from a tree's trunk to the edge of the shadow your task is to calculate and return an integer value representing the shadow area of the canopy

Note round off the resort to the nearest integer value

input : D = 5
output : 78
"""

def area(D:int)->int:
    return round((3.14)*(D**2))

D = int(input())
print(area(D))