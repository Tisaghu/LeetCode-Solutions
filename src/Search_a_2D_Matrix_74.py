

class Solution(object):
    def searchMatrix(self, matrix, target):
        #first do a binary search on the rows to find out which one it's in
        low, high = 0, len(matrix)-1
        rowLength = len(matrix[0])-1
        targetRow = None

        while low != high:
            mid = (low + high) // 2
            if matrix[mid][0] < target < matrix[mid][rowLength]:
                targetRow = mid
                break
            elif target > matrix[mid][rowLength]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1

        print(targetRow)


test = Solution()
test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)




