"""
You are given two integers A and B a represents the coordinates on the X axis(0,A) and B Represents the coordinate on the Y axis(B,0)

These are the two coordinate points of a right angle triangle the Third Point being the origin (0,0). You will be given N Such triangles in the input find out and print the length of the hypotenuse of all the triangles

Note : 
The formula of the length of the hypotenuse = root(a^2 + b^2) Where A and B represents the length of the other two sides of the triangle
If the length of the hypotenuse is in the decimal round it to the next greatest integer

Input format:
The input consist is given in the following format:
The first line contains an integer N denoting the number of triangles
The next end line contains two space separated integer representing A and B respectively
The input will be read from the STDIN By the candidate

Output format:
The output consists of N lines:
Each line representing the length of the hypotenuse of the T triangle

"""
import math

def hypo(a:int,b:int)->int:
    return math.ceil(((a**2) + (b**2)) ** (1/2))

testCase = int(input())
for i in range(testCase):
    a,b = map(int,input().split())
    print(hypo(a,b))