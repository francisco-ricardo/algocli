# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def run(nums: list[int]) -> int:
    '''
    The function receives a sorted array of integers as a parameter.
    It should remove the duplicates in-place such that each element appears only once and returns the new length.
    Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
    
    Approach
    ---------
    Use two pointers to iterate the array.
    The first pointer, slow, will point to the last unique element.
    The second pointer, fast, will iterate the array.
    If nums[slow] != nums[fast], increment slow and assign nums[slow] = nums[fast].
    Return the length of the unique elements.
    
    Time: O(n)
    Space: O(1)
    
    Parameters
    -----------
    1. nums: input array (integers)
    
    '''
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
        
