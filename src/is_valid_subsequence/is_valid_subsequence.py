'''
Given two non-empty arrays of integers, write a function that 
determines whether the second array is a subsequence of the 
first one. 

'''

def isValidSubsequence(array, sequence):
    '''
    Checks if the second array is a subsequence of the 
    first one.

    Parameters
    ----------
    array: the main array
    sequence: the potential subsequence array

    Approach
    ---------
    The function defines the sequenceIndex variable to hold the index 
    of the potential subsequence array element, starting as 0.
    Iterates over the main array and increments by one the 
    sequenceIndex value when the main element value 
    is equal to the sequence array value at the sequenceIndex position.
    The iteration stops whenever the sequenceIndex is equal to
    the length of the sequence array.
    The return is the logical value of the comparison between 
    sequenceIndex and the length of the sequence array.

    Time: O(n)
    Space: O(1)

    Notes
    -----
    - Following the Camel Case standard for naming functions and variables, 
      despite that the Snake Case is more common in Python coding.

    '''
    sequenceIndex = 0

    for i in array:
        if (sequenceIndex == len(sequence)):
            break
        if (sequence[sequenceIndex] == i):
            sequenceIndex += 1

    return (sequenceIndex == len(sequence))
