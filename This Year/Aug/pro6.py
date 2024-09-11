"""
Snake water gun

You are given a string as which contains most played by the player Sequentially in a game called Snakewater Gun The rules of the games are as follows:

Snake beats water, Water beats gun and Gun beat snake.

The move played by Player A and the move played by the player B in the first round will be stored in the string as snakewater

Similarly in the second round the mouse will be stored in a string as snakewatergunsnake
There total n rounds that are played in the game and your task is to find and return an integer value representing how many rounds player a wins 

"""

def win(String:str)-> int:
    i = 0
    AWin = 0
    while(i < len(String)):
        if String[i] == 's' and String[i+5] == 'w':
            AWin +=1
            i+=10
        elif String[i] == 's' and String[i+5] == 'g':
            i+=8
        elif String[i] == 'w' and String[i+5] == 'g':
            AWin +=1
            i+=8
        elif String[i] == 'w' and String[i+5] == 's':
            i+=10
        elif String[i] == 'g' and String[i+3] == 's':
            AWin +=1
            i+=8
        else :
            i+=8
    return AWin

String = input()
print(win(String=String))