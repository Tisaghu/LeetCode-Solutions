from src.Search_a_2D_Matrix_74 import Solution


import pytest

test_cases = [
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
    ([[1]], 1, True),
    ([[1]], 0, False),
    ([[1],[3]], 2, False)
]

@pytest.mark.parametrize("matrix, target, expected", test_cases)
def test_searchMatrix(matrix, target, expected):
    solver = Solution()
    result = solver.searchMatrix(matrix, target)
    assert result == expected