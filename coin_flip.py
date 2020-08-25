# Coin Flip Simulation
# Create a program that uses Python’s random number generator to simulate flipping
# a coin several times. The simulated coin should be fair, meaning that the probability
# of heads is equal to the probability of tails. Your program should flip simulated
# coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
# time the outcome is heads, and a T each time the outcome is tails, with all of the
# outcomes shown on the same line. Then display the number of flips needed to reach
# 3 consecutive flips with the same outcome. When your program is run it should
# perform the simulation 10 times and report the average number of flips needed.

import random

def coin_flip():
    coin = []
    numval = 0
    for i in range(10000):
        ht = random.randint(0,1)
        if ht == 0:
            coin.append('H')
        elif ht == 1:
            coin.append('T')
        if i > 5:
            if coin[i] == coin[i-1] and coin[i] == coin[i-2] and coin[i] == coin[i-3] and coin[i] == coin[i-4] and coin[i] == coin[i-5] and coin[i] == coin[i-6]:
                numval += 1
    chance_of_streak = (numval/10000)*100
    print(coin)
    print('Coin Flip Streaks are: ', numval)
    print("Chance of streak: ""{:.2f}".format(chance_of_streak) + '%')

coin_flip()
