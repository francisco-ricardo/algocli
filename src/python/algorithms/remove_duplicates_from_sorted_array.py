"""
Given an integer array nums sorted in non-decreasing order, remove 
the duplicates in-place such that each unique element appears only 
once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get 
accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain 
the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size 
of nums. Return k.
"""

def run(nums: list[int]) -> int:
    """
    Removes duplicates from a sorted array in-place.

    Parameters
    ----------
    nums: the sorted array of integers

    Approach
    ---------
    The function uses two pointers to iterate through the array. 
    The first pointer (slow) keeps track of the position of the last 
    unique element, while the second pointer (fast) iterates through 
    the array. If a new unique element is found, it is placed at 
    the position of the first pointer, and the first pointer is 
    incremented.

    Time: O(n)
    Space: O(1)

    """    
    if not nums:
        return 0
    
    slow = 0  # Pointer for the last unique element
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1

# EOF