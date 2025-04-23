"""
Write a function or method that takes 2 strings as inputs and returns
a boolean specifying whether a substring of the first string is an 
anagram of the second.

Examples:
“aaaaaabacbaaa”, “baca” -> true
“aaaabaaaaacaa”, “baca” -> false

"""
import sys
from collections import Counter


def is_anagram(first: str, second: str) -> bool:
    """
    The function receives two strings as parameters.
    It should return a boolean indicating whether a substring of the 
    first string is an anagram of the second.    

    Parameters
    -----------
    1. first: input string (characters)
    2. second: input string (characters)

    """   

    # Edge cases
    if not first or not second or len(first) < len(second):
        return False

    # Using Counter objects to count the frequency of characters
    second_char_count = Counter(second)
    window_char_count = Counter()

    for i in range(len(first)):
        window_char_count[first[i]] += 1

        if i >= len(second):
            if window_char_count[first[i - len(second)]] == 1:
                del window_char_count[first[i - len(second)]]
            else:
                window_char_count[first[i - len(second)]] -= 1

        if window_char_count == second_char_count:
            return True

    return False


def test():
    """
    Test the function `is_anagram` with some test cases.
    """
    assert is_anagram("aaaaaabacbaaa", "baca") == True
    assert is_anagram("aaaabaaaaacaa", "baca") == False
    assert is_anagram("abcde", "cde") == True


if __name__ == "__main__":    

    if (len(sys.argv) == 2):
        test()
        print("All tests passed.")
        sys.exit(0)
    elif (len(sys.argv) == 3): 
        first = sys.argv[1]
        second = sys.argv[2]
        result = is_anagram(first, second)
        print(f"Is an anagram: {result}")
    else:
        print("Invalid number of arguments.")
        print("Please provide two strings to compare.")
        print("Example: python anagrams_ssc.py 'aaaaaabacbaaa' 'baca'")
        print("Example: python anagrams_ssc.py 'aaaabaaaaacaa' 'baca'")
        print ("Or run the test cases with:")
        print("Usage: python anagrams_ssc.py test")
        sys.exit(1)
    

    # EOF
