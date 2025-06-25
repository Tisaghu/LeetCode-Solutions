import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        #maximum value of k is the value of the largest pile
        lower_bound, upper_bound = 1, max(piles)
        res = upper_bound

        #check values of k between 1 and max(piles) using binary search
        while lower_bound <= upper_bound:
            k = (lower_bound + upper_bound) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / k)

            if totalTime <= h:
                res = k
                upper_bound = k - 1
            else:
                lower_bound = k + 1
        return res
        
