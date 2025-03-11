class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #need to find three numbers x,y and z such that x + y + z = 0
        #if I fix one of those numbers, then I need to find two numbers that add up to the negative of that number
        #I can use the two sum approach to find those two numbers
        #I only need two pointers I think
        #I can sort the array first to make it easier to find the two numbers

        #sort the array
        nums.sort()
        result = []
        seen = []

        #it's like the 2sum problem with x being the target number
        for i in range(0,len(nums)-1):
            fixed = nums[i]
            target = -fixed
            seen.append(fixed)

            #now I need to find two numbers that add up to target that are not the fixed number
            for j in range(0,len(nums)-1):
                if j == i:
                    continue
                diff = target - nums[j]
                if diff in seen:
                    triplet = [fixed, diff, nums[j]]








test = Solution()
print(test.threeSum([-1,0,1,2,-1,-4])) #[[-1,-1,2],[-1,0,1]]
print(test.threeSum([0,1,1])) #[]
print(test.threeSum([])) #[]

