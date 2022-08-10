#!/usr/bin/python3
'''
Module 0-making_change
Contains function makeChange()
'''


def makeChange(coins, total):
    '''
    coins is a list of the values of the coins in your possession
    Return: fewest number of coins needed to meet total
    '''

    coins = list(reversed(sorted(coins)))
    # print("Coins:", coins, "\nTotal", total)

    coins_needed = 0
    coins_remaining = -1

    if total % coins[0] == 0:
        return int(total / coins[0])

    for i in coins:
        # print("i:", i)
        # print("Before: coins_needed:", coins_needed,
        #      "coins_remaining", coins_remaining)
        if coins_remaining == -1:
            coins_remaining = total % i
            coins_needed += total // i
            # print("After: coins_needed:", coins_needed,
            #      "coins_remaining", coins_remaining)
            continue

        if coins_remaining % i == 0:
            if coins_remaining == 0:
                coins_needed += total / i
            else:
                coins_needed += coins_remaining / i
            # print("After: coins_needed:", coins_needed,
            #      "coins_remaining", coins_remaining)
            coins_remaining = 0
            break

        if coins_remaining >= i:
            coins_remaining %= i
            coins_needed += 1
        # print("After: coins_needed:", coins_needed,
        #      "coins_remaining", coins_remaining, '\n')

    return int(coins_needed) if coins_remaining == 0 else -1
