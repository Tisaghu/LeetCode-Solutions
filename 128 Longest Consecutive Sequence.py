class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #create a set
        numSet = set(nums)
        checked = set()
        longest = 0

        for n in nums:
            if n not in checked:   
                #check for (n-1) -> this num is the start of a sequence
                if (n-1) not in numSet:
                    length = 0
                    while(n+length) in numSet:
                        length +=1
                    longest = max(length,longest)
                checked.add(n)
        return longest
            

        

test = Solution()
nums = [100,4,200,1,3,2]
print(test.longestConsecutive(nums))