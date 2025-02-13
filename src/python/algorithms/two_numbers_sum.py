
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def run(nums: list[int], target: int) -> list[int]:
    '''
    The function receives an array and an integer as parameters.
    If any two numbers in the input array add up to the target value,    
    it should return the corresponding indices, in any order.
    If no two numbers add up to the target sum, the function should
    return an empty list.

    Approach
    ---------
    Use a hash map (a dictionary in Python) to store visited elements indices.
    For each number in the array, check whether target - nums[i] exists in the dictionary.
    If it does, we found the pair and return their indices.    

    Time: O(n)
    Space: O(n)

    Parameters
    -----------
    1. nums: input array (integers)
    2. target: the target value (integer) for testing the input array

    '''
    potential_nums = dict()
    for index, num in enumerate(nums):
        potential_num = target - num
        if (potential_num in potential_nums.keys()):
            return [index, potential_nums[potential_num]]
        potential_nums[num] = index
    return []

