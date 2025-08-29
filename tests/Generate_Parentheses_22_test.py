import pytest
from src.Generate_Parentheses_22 import Solution

test_cases = [
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (1, ["()"]),
    (2, ["()()", "(())"])
]

@pytest.mark.parametrize("n, expected", test_cases)
def test_generate_parenthesis(n,expected):
    solver = Solution()
    result = solver.generateParenthesis(n)
    assert set(result) == set(expected)