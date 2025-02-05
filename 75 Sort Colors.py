#Problem 1: Sort Colors (LeetCode #75)
#You are given an array nums with integers 0, 1, and 2 representing colors. Sort the array in-place so that elements of the same color are adjacent, in the order 0, 1, 2.

#Input: nums = [2, 0, 2, 1, 1, 0]
#Output: [0, 0, 1, 1, 2, 2]
#Hint: Use a variation of the Quick Sort partitioning technique.

#recursively called function
def sort_colors(nums):
    #if length of the array is less than or equal to 1 then return it
    if len(nums) <= 1:
        return array
    
    #pick a pivot - in this case the last element of the array
    pivot = nums[-1]

    #create new left and right arrays based on pivot - EXCLUDING THE PIVOT
    left = [num for num in array[:-1] if num <= pivot]
    right = [num for num in array[:-1] if num > pivot]

    #recursive return statement - calling on new right and left arrays plus the pivot
    return sort_colors(left) + [pivot] + sort_colors(right)


#Optimized approach:
# Use three pointers:
# low: Marks the boundary of 0's
# high: Marks the boundary of 2's
# current: Iterates through the array

#Algorithm Steps:
# 1. If the current element is 0, swap it with low and move both pointers
# 2. If the current element is 2, swap it with high and only move high backwards
# 3. If the current element is 1, simply move the current pointer

def sort_colors(nums):
    low, current, high = 0, 0, len(nums) - 1

    while current <= high:
        if nums[current] == 0:
            nums[low], nums[current] = nums[current], nums[low]
            low += 1
            current += 1
        elif nums[current] == 2:
            nums[high], nums[current] = nums[current], nums[high]
            high -= 1
        else:  # nums[current] == 1
            current += 1


#Why this approach?
# Time Complexity: O(n), since we traverse the array once
# Space Complexity: O(1), as no extra data structures are used.
# Optimal for Three Values: Tailored to problems with a small, fixed set of distinct elements.
