import pytest
from Valid_Parentheses_20 import Solution

test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False ) 
]

@pytest.mark.parametrize("s, expected", test_cases)
def test_minEatingSpeed(s, expected):
    solver = Solution()
    result = solver.isValid(s)
    assert result == expected

