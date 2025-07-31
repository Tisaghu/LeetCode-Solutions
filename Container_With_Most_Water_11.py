class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r  = 0, len(height)-1
        maxArea = 0

        while l != r:
            area = (r-l) * min(height[l], height[r])
            maxArea = max(maxArea, area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea

        
        


test = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(test.maxArea(height)) #49

height = [1,1]
print(test.maxArea(height)) #1