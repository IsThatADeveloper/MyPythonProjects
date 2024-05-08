import random
from art import draw
import os

choices = ['rock', 'paper', 'scissors']

def determine_winner(player, opp):
    if player == opp:
        return('Its a tie game!')
    elif ((player == 'rock' and opp == 'scissors') or 
          (player == 'paper' and opp == 'rock') or 
          (player == 'scissors' and opp == 'paper')):
            return('You Won!')
    else: 
        return('Opponent Won, sorry!')

playing, invalid = True, False

os.system('cls' if os.name == 'nt' else 'clear')

while playing:
    if not invalid:
        print('Choose rock, paper or scissors')
    else:
        print('Invalid input, please type rock, paper, or scissors')
        invalid = False
    print('Or enter q to quit')

    player_choice = input().lower().strip()

    opp_choice = random.choice(choices)

    if player_choice in choices:
        print('You chose: ' + player_choice + draw(player_choice))
        print('The opponent chose: ' + opp_choice + draw(opp_choice))
        print(determine_winner(player_choice, opp_choice))
        playing = False
        
        print("Do you want to rematch (Y|N):") 
        rematch = input().lower().strip()
        if(rematch == 'y' and not invalid):
            playing = True

            os.system('cls' if os.name == 'nt' else 'clear')

        elif(rematch == 'n' and not invalid):
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('Thank you for playing!')

        else:
            invalid = True
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('Invalid input, the game has ended')
            print('Thank you for playing!')

    elif player_choice == 'q':
        playing = False
        print('You chose quit, thank you for playing!')
    else:
        invalid = True



    