import random

# get the number of dice from user
num_dice = int(input("How many 6-sided dice do you want to roll? (integer only) "))

# generate a random number between 1 and 6 (inclusive) for each die 
print("You rolled:", end=" ")
for _ in range(num_dice):
    dice_roll = random.randint(1,6)
    print(dice_roll, end=" ")

# print new line / prevent "%" from showing up in terminal after the dice rolls
print()