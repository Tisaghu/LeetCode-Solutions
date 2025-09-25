import pytest
from src.Longest_Substring_Without_Repeating_Characters_3 import Solution

test_cases = [
    ("aab", 2),
    ("", 0),
    ("abcabcbb", 3)
]

@pytest.mark.parametrize("s, expected", test_cases)
def test_lengthOfLongestSubstring(s, expected):
    solver = Solution()
    result = solver.lengthOfLongestSubstring(s)
    assert result == expected
