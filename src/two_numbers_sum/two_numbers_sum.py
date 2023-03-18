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

    Parameters
    -----------
    1. array: input array (integers)
    2. targetSum: the target value (integer) for testing the input array

    Notes
    -----
    - The camel case is not common for naming functions in Python. 
      But it seems like it is a standard for Algo Expert. 
      So I decided to follow the Algo Exert standard and name the 
      functions using camel case.
    - Algo Expert asks for only one function for the solution. 
      They even indicated the name of the function. So, I decided to 
      create only one function and create helper functions inside it.

    '''
    # Helper function
    def _pairsGenerator(array):
        '''
        Generator function that receives an array as input 
        and yield tuples of pairs of elements.
        
        Example:
        [1, 2, 3] -> ((1, 2), (1, 3), (2, 3))
        '''
        pair_heads_index = [x for x in range(0, (len(array) - 1))]
        pair_tails_index = [x for x in range(1, len(array))]
        for i in pair_heads_index:
            for j in pair_tails_index:
                if (j <= i):
                    continue
                yield(array[i], array[j],)


    # Helper function
    def _pairSum(pairsArray, targetSum):
        '''
        Helper function that receives two arguments:
        1. Array of tuples (integers)
        2. Target sum (integer)
        
        Each tuple has two integers. The function loops over the array.
        If a tuple sum up to the target sum, the function returns the 
        two elements as an array.
        If no tuple sum up to the target sum, the function returns an 
        empty array.        
        '''
        for pair in pairsArray:
            if (pair[0] + pair[1] == targetSum):
                return [pair[0], pair[1]]
        else:
            return []

        
    # Main
    pairsArray = [x for x in _pairsGenerator(array)]
    result = _pairSum(pairsArray, targetSum)
    return result
