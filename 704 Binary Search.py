class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)-1

        while(lo <= hi):
            #find the halfway point of the array
            mid = (lo + hi) // 2

            #check if mid is the target
            if nums[mid] == target:
                return mid
            else:
                #check if target is to the right or left of mid
                if target < nums[mid]:
                    #mid is the new hi
                    hi = mid - 1
                else:
                    #mid is the new lo
                    lo = mid + 1
        return -1


test = Solution()
nums = [-1,0,3,5,9,12]
target = 2
print(test.search(nums, target)) 