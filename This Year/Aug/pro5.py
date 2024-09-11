"""
Vacant rooms

You are a manager of a hotel You have a list of rooms already reserved in an array A of size N You also have the total number of rooms T. Your task is to find and return the integer value representing the total number of vacant rooms.

Input specifications:
Input1 : An integer array A representing the reserved rooms
Input2 : An integer value and representing the count of reserved room
Input3 : An integer value representing the total number of rooms

Output specifications:
Return the integer value representing the total number of vacant rooms
"""

def vacantRooms(total : int ,reserved :int)->int:
    return total - reserved

 
arr = list(map(int,input().split()))
reserved = int(input())
total = int(input())

print(total,reserved)