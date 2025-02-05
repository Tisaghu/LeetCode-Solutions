class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #keep track of numbers already seen with a hash map
        #key = the number , value = the index
        seen = {}

        #iterate through nums
        for i in range(0, len(nums)):
            #check for solution
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]

            #add to hash map
            seen[nums[i]] = i




test = Solution()
print(test.twoSum([3,2,4], 6)) #[1, 2]
print(test.twoSum([2,7,11,15], 9)) #[0, 1]
