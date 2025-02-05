class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #need two pointers
        #l = buy, r = sell
        l, r = 0, 1
        profit = 0

        while r <= len(prices)-1:
            if prices[l] <= prices[r]:
                profit = max(profit, prices[r]-prices[l])
                #update r
                r += 1
            elif prices[r] < prices[l]:
                #this is a new minimum, update l
                l = r
                r = l + 1
        return profit

        
test = Solution()
print(test.maxProfit([3,3])) #5