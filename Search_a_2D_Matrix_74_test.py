import pytest
from Search_a_2D_Matrix_74 import Solution

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

