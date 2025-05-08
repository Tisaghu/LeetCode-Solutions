import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #Use a max heap disguised as a min heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            #pop the top two stones from the max heap
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: #Greater because using negative numbers to simulate max heap
                heapq.heappush(stones, second - first)

        stones.append(0)
        return abs(stones[0])



    

test = Solution()
stones = [2,7,4,2,8,1]
print(test.lastStoneWeight(stones)) #1