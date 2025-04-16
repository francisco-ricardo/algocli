"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

def run(nums: list[int], target: int) -> int:
    """
    Searches for the target in the sorted array.

    Parameters
    ----------
    nums: the sorted array
    target: the number to search

    Approach
    ---------
    The function defines two pointers, left and right, which are set to 
    the start and end of the array, respectively. It then enters a loop 
    that continues until the left pointer is greater than the right 
    pointer. Inside the loop, it calculates the middle index and checks 
    if the value at that index is equal to the target. If it is, it 
    returns the index. If the value is less than the target, it moves 
    the left pointer to mid + 1. If it is greater than the target, it 
    moves the right pointer to mid - 1. If the loop completes without 
    finding the target, it returns -1.

    Time: O(log n)
    Space: O(1)

    """
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1