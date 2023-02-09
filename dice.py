import random

DICE = [
        (" ------- ",
         "|       |",
         "|   o   |",
         "|       |",
         " ------- "),
        (" ------- ",
         "| o     |",
         "|       |",
         "|     o |",
         " ------- "),
        (" ------- ",
         "| o     |",
         "|   o   |",
         "|     o |",
         " ------- "),
        (" ------- ",
         "| o   o |",
         "|       |",
         "| o   o |",
         " ------- "),
        (" ------- ",
         "| o   o |",
         "|   o   |",
         "| o   o |",
         " ------- "),
        (" ------- ",
         "| o   o |",
         "| o   o |",
         "| o   o |",
         " ------- "),
]

def dice_roll():
    user_input = input("press enter to play or q to quit: ")
    dice_value_list = [] ## stores all dice rolls in the game as list
    counter_one = 0  ## count the number of rounds played
    while True:

        if user_input == "": ## any input will throw you out to the else statment
            counter_one += 1
            dice_num_one = random.randint(1, 6) ## gives a random int
            dice_num_two = random.randint(1, 6) ##same
            rolled_dice = (dice_num_one, dice_num_two)
            dice_value = dice_num_one + dice_num_two
            dice_value_list.append(dice_value)

            for i in range(5):
                for die in rolled_dice:
                    print(DICE[die-1][i], end= ' ')
                print()
            print(sum(rolled_dice))
            user_input = input("press enter to play or q to quit: ")
        else:
            print("thanks for playing!")
            for i in range(2, 13):
                count = dice_value_list.count(i)
                rolL_chance = (count * 100)/counter_one
                print(str(i)+":", count, "times,", str(rolL_chance)+"%")
            print()
            break
def main():
   dice_roll()

main()