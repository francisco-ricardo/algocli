
# TODO: o algoritmo baseado em two pointers funcionaria somente se o array estivesse ordenado
## implementar um novo algoritmo baseado em hashmap.

def run(nums: list[int], target: int) -> list[int]:
    '''
    The function receives an array and an integer as parameters.
    If any two numbers in the input array sum up to the target sum,
    it should return the corresponding indices, in any order.
    If no two number sum up to the target sum, the function should
    return an empty array.

    Approach
    ---------
    

    Time: O(n)
    Space: O(1)

    Parameters
    -----------
    1. nums: input array (integers)
    2. target: the target value (integer) for testing the input array

    '''

    potential_nums = dict()
    for index in range(len(nums)):
        potential_num = target - nums[index]
        if (potential_num in potential_nums.keys()):
            return [index, potential_nums[potential_num]]
        else:
            potential_nums[potential_num] = index
    return []


    # left = 0
    # right = len(nums) - 1
    # while left < right:
    #     current_sum = nums[left] + nums[right]
    #     if (current_sum == target):
    #         return [left, right]
    #     elif (current_sum < target):
    #         left += 1
    #     else:
    #         right -= 1

    # return []


