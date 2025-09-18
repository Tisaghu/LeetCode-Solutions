import pytest
from src.Daily_Temperatures_739 import Solution

test_cases = [
    ([73,74,75,71,69,72,76,73],[1,1,4,2,1,1,0,0],
     [30,40,50,60],[1,1,1,0],
     [30,60,90],[1,1,0])
]

@pytest.mark.parametrize("temperatures, expected", test_cases)
def test_generate_parenthesis(temperatures,expected):
    solver = Solution()
    result = solver.dailyTemperatures(temperatures)
    assert result == expected