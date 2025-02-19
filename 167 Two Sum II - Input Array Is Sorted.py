class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #use two pointers
        left, right = 0, len(numbers) - 1

        while left < right:
            #calculate the sum of the two pointers
            total = numbers[left] + numbers[right]

            #check if the sum is equal to the target
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1





test = Solution()
print(test.twoSum([2,7,11,15], 9)) #[1, 2]
print(test.twoSum([2,3,4], 6)) #[1, 3]
print(test.twoSum([-1,0], -1)) #[1, 2]