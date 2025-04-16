"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged 
to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be 
rearranged to form each other.
"""

def run(strs: list[str]) -> list[list[str]]:
    """
    Groups the anagrams together.

    Parameters
    ----------
    strs: the array of strings

    Approach
    ---------
    The function initializes a dictionary to hold the anagrams. 
    It then iterates over each string in the input array, sorts 
    the string, and uses the sorted string as a key in the 
    dictionary. The original string is appended to the list 
    corresponding to that key. Finally, it returns the values 
    of the dictionary as a list of lists.

    Time: O(n * k log k)
    Space: O(n)

    """
    
    anagrams = {}
    
    for s in strs:
        # Sort the string and use it as a key
        key = ''.join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    
    return list(anagrams.values())