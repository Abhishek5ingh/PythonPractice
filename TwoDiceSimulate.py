# In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function that simulates rolling a pair of six-sided dice. Your function will not take any
# parameters. It will return the total that was rolled on two dice as its only result.
# Write a main program that uses your function to simulate rolling two six-sided
# dice 1,000 times. As your program runs, it should count the number of times that each
# total occurs. Then it should display a table that summarizes this data. Express the
# frequency for each total as a percentage of the total number of rolls

import random
def two_dice_sim():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1+dice2

def main():
    dice_dict = {}
    for i in range(2,13):
        dice_dict.setdefault(i,0)
    #roll_dice = two_dice_sim()
    for dice_cnt in range(1000):
        roll_dice = two_dice_sim()
        dice_dict[roll_dice] += 1
    #print(dice_dict)
    print('Total   ' + '   Simulated Percent')
    for key in dice_dict.keys():
        perc = round((dice_dict[key]/1000)*100,2)
        print(str(key) + '          ' + str(perc))

if __name__ == "__main__":
    main()
