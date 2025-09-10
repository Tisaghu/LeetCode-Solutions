import pytest
from src.Longest_Repeating_Character_Replacement_424 import Solution

test_cases = [
    ("ABAB",2),
    ("AABABBA",1)
]

@pytest.mark.parametrize("s, k, expected", test_cases)
def test_characterReplacement(s, k, expected):
    solver = Solution()
    result = solver.characterReplacement(s,k)
    assert result == expected

