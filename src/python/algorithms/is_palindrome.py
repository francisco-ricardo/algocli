"""
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters 
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

def run(s: str) -> bool:
    """
    Checks if the string is a palindrome.

    Parameters
    ----------
    s: the string to check

    Approach
    ---------
    The function defines two pointers, left and right, which are set to 
    the start and end of the string, respectively. It then enters a loop 
    that continues until the left pointer is greater than or equal to 
    the right pointer. Inside the loop, it checks if the characters at 
    the left and right pointers are equal (after converting them to 
    lowercase and removing non-alphanumeric characters). If they are not 
    equal, it returns False. If they are equal, it increments the left 
    pointer and decrements the right pointer. If the loop completes 
    without returning False, it returns True.

    Time: O(n)
    Space: O(1)

    """
    
    left = 0
    right = len(s) - 1

    while left <= right:
        while left < len(s) and not s[left].isalnum():
            left += 1
        while right >= 0 and not s[right].isalnum():
            right -= 1

        if left > right:
            break

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
