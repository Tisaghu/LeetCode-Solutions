class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #Brute force solution that runs out of time
        #TODO: Come back to this and find effeciency
        l = 0
        res = 0

        while l < len(height):
            r = l+1
            while r < len(height):   
                segWidth = r - l
                area = min(height[l], height[r]) * segWidth
                if area > res:
                    res = area
                r+=1
            l += 1
        return res
        


test = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(test.maxArea(height)) #49

height = [1,1]
print(test.maxArea(height)) #1