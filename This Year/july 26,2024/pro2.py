"""
Rock paper and scissors:

Two players a and B are playing a game of rock paper and scissors player a chooses a move represented by string M and move can be one of the following rock paper or scissor
where 1 - Rock beats scissors 
      2 - scissors beats paper
      3 - paper beats rock

Your task is to find and return a string value representing the winning move of B

input : rock
output : paper

input : paper
output : scissors

input : scissors
output : rock

"""

player_A = input().lower()

if player_A == "scissors" :
    print("rock")
elif player_A == "paper":
    print("scissors")
else :
    print("paper")


