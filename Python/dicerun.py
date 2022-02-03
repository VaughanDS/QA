# In the second file, use the dice module to simulate throwing 2 dice,
# Print the values you get from the dice.

from dice import diceroll


def throws():
    dice1 = diceroll()
    dice2 = diceroll()
    throw = dice1 + dice2
    return f"Dice 1 = {dice1} \n Dice 2 = {dice2} \n Total = {throw}"


print(throws())
