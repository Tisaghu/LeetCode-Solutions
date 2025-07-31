class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        res = 0

        while l < r:
            area = min(height[l], height[r]) * (r-l)
            print(area)
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return res


test = Solution()

input = [1,8,6,2,5,4,8,3,7]
test.maxArea(input)