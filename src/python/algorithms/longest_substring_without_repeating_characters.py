"""
Given a string s, find the length of the longest substring without 
duplicate characters.
"""

def run(s: str) -> int:
    """
    The function receives a string as a parameter.
    It should return the length of the longest substring without 
    repeating characters.

    Approach
    ---------
    Use a hash set to store the characters in the current substring.
    Use two pointers to represent the start and end of the substring.
    If a character is already in the set, move the start pointer to 
    the right until the character is removed from the set.
    
    Time: O(n)
    Space: O(min(n, m)), where n is the length of s and m is the size 
    of the charset/alphabet.

    Parameters
    -----------
    1. s: input string (characters)

    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length