class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sort the array
        nums.sort()
        result = []

        #it's like the 2sum problem with x being the target number
        for i in range(0,len(nums)-1):
            fixed = nums[i]
            target = -fixed

            #Since the array is sorted, can use a two pointer approach to efficiently find j and k
            j, k = i + 1, len(nums)-1
            while j < k:
                currentSum = nums[j] + nums[k]
                if currentSum == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                if currentSum > target:
                    k -= 1
                else:
                    j += 1

        return result










test = Solution()
print(test.threeSum([0,0,0,0]))
print(test.threeSum([-1,0,1,2,-1,-4])) #[[-1,-1,2],[-1,0,1]]


