"""
Rebound height

Daniel has a ball he wants to find the balls rebound height which he dropped from the height H With an initial velocity V After the nth rebound the final velocity of the ball is Vn Your task is to help him find and return an integer value representing the height to which the ball rebounds after N bounces 

Note :
H' = H*e^2n Where H' is the rebound height H is the initial height E is the coefficient of restitution and N is the number of bounces

e^n = v/V^n Where V is the initial velocity and VN is the final velocity
"""

def BounceHeigth(height,initial,final)->int:
    return height * ((initial/final)**2)

height = int(input())
initial = int(input())
final = int(input())

print(BounceHeigth(height,initial,final))