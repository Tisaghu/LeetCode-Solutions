class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Bucket sort implementation
        # Time complexity: O(n)
        # Space complexity: O(n)
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            #update the frequency dictionary, add one or make it 0 if not seen before
            count[num] = 1 + count.get(num, 0)

        #for every key value pair in the dictionary    
        for num, cnt in count.items():
            #append the number to the list at the index of its frequency
            freq[cnt].append(num)

        res = []
        #from the last index to 0, moving backwards
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

#Test Cases
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2)) #[1,2]
print(s.topKFrequent([1], 1)) #[1]
print(s.topKFrequent([1,2], 2)) #[1,2]