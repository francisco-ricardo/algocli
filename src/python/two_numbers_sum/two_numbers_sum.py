'''
Two Number Sum

Write a function that takes in a non-empyt array of distinct integers
and an integer representing a target sum. If any two numbers in the
input array sum up to the target sum, the function should return them
in an array, in any order. If no two number sum up to the target sum,
the function should return an empty array.

Note that the target sum has to be obtained by summing two different
integers in the array; you can not add a single integer to itself in
order to obtain the target sum.

'''

def twoNumberSum(array, targetSum):
    '''
    The function receives an array and an integer as parameters.
    If any two numbers in the input array sum up to the target sum, 
    it should return them in an array, in any order. 
    If no two number sum up to the target sum, the function should 
    return an empty array.

    Approach
    ---------
    targetSum = currentNum + potentialNum
    potentialNum = targetSum - currentNum

    Time: O(n)
    Space: O(n)

    Parameters
    -----------
    1. array: input array (integers)
    2. targetSum: the target value (integer) for testing the input array

    Notes
    -----
    - Following the Camel Case standard for naming functions and variables, 
      despite that the Snake Case is more common in Python coding.

    '''
    potentialNums = set()
    for i in array:
        potentialNum = targetSum - i
        if (potentialNum in potentialNums):
            return [i, potentialNum]
        else:
            potentialNums.add(i)
    
    return []

# EOF


