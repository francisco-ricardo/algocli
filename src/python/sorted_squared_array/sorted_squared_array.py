'''
Write a function that takes in a non-empty array of integers
that are sorted in ascending order and returns a new array
of the same length with the squares of the original integers
also sorted in ascending order.

Example:
array = [-10, 1, 2, 3, 5, 6, 8, 9]
output = [1, 4, 9, 25, 36, 64, 81, 100]

'''


def sortedSquaredArray(array):
    '''
    Receives a sorted array as input and returns a new sorted array
    with the squared values.

    Parameters
    ----------
    array: input array (integers)

    Approach
    ---------
    Defines a reference for the smaller values (head) and a referece
    for the grater values (tail), assuming the list is sorted.
    Traverses the input array in reverse order and compares the head 
    value against the tail value. The greater value is placed into the 
    output array in the current position. The current index is 
    decremented. Either the head index or the tail index is moved 
    according to the comparison.

    Time: O(n)
    Space: O(n)

    Notes
    -----
    - Following the Camel Case standard for naming functions and variables, 
      despite that the Snake Case is more common in Python coding.

    '''
    headIndex = 0
    tailIndex = len(array) - 1
    currentIndex = len(array) - 1
    outputArray = [0 for x in array]
    while (currentIndex >= 0):
        headValue = abs(array[headIndex])
        tailValue = abs(array[tailIndex])
        if (tailValue >= headValue):
            outputArray[currentIndex] = (tailValue * tailValue)
            tailIndex -= 1
        else:
            outputArray[currentIndex] = (headValue * headValue)
            headIndex += 1
        currentIndex -= 1
    return outputArray

# EOF
