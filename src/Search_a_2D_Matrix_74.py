class Solution(object):
    def searchMatrix(self, matrix, target):
        #first do a binary search on the rows to find out which one it's in
        low, high = 0, len(matrix)-1
        rowLength = len(matrix[0])-1
        targetRow = None

        # Handle edge case 
        if target > matrix[high][rowLength] or target < matrix[low][0]:
            return False

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][rowLength]:
                targetRow = matrix[mid]
                break
            elif target > matrix[mid][rowLength]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
        
        if targetRow == None:
            return False

        # Do a second binary search in the target row
        l, r = 0, rowLength

        while l <= r:
            mid = (l+r) // 2
            if targetRow[mid] == target:
                return True
            elif target > targetRow[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False
