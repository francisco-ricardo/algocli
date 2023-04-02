'''
Given an array of positive integers representing the values of coins
in your possession, write a function that returns the minimum amount
of change (the minimum sum of money) that you can not create.
The given coins can have any positive integer value and are not 
necessarily unique (i.e., you can have multiple coins of the same 
value).

Examples:
coins = [5, 7, 1, 1, 2, 3, 22]
output = 20

coins = [1, 2, 5]
output = 4

coins = []
output = 1

'''


def nonConstructibleChange(coins):
    '''
    Receives an array of coins and returns the minimum amount of change
    that can not be created with the coins.

    The input array is not necessarily sorted.

    Parameters
    ----------
    coins: input array (integers)

    Approach
    ---------

    The array of coins can be empty or composed of positive integers.

    u = {0} OR {n : n E Z+ AND n > 0}
    Where,
    u = the array of coins
    n = a coin

    The algorithm to define the minimum change is based on the rules 
    below:

    v > c + 1 => c + 1    (1)
    v <= c + 1 => c + v   (2)

    Where,
    v: the next coin in the array
    c: the current change created

    Time: O(n log n)
    Space: O(1)

    Notes
    -----
    - Following the Camel Case standard for naming functions and variables, 
      despite that the Snake Case is more common in Python coding.    

    '''
    coins.sort()
    change = 0
    for coin in coins:
        if (coin > (change + 1)):
            return (change + 1)
        else:
            change += coin
    return (change + 1)

# EOF
