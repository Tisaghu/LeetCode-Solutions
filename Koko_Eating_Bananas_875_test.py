import pytest
from Koko_Eating_Bananas_875 import Solution

test_cases = [
    ([3,6,7,11], 8, 4),
    ([30,11,23,4,20], 5, 30),
    ([30,11,23,4,20], 6, 23),
    ([25,10,23,4], 4, 25)
]

@pytest.mark.parametrize("piles, h, expected", test_cases)
def test_minEatingSpeed(piles, h, expected):
    solver = Solution()
    result = solver.minEatingSpeed(piles, h)
    assert result == expected