from art import dice_art
import random
import os

dice = []

total = 0

os.system('cls' if os.name == 'nt' else 'clear')  

num_of_dice = int(input('Number of dice?: '))

for num in range(num_of_dice):
    dice.append(random.randint(1,6))

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die

print(f'total: {total}')

