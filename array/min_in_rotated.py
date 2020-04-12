# https: // leetcode.com/problems/find-minimum-in-rotated-sorted-array/
import math

def findMin(nums):
    low = 0
    high = len(nums) - 1

    while (low < high):
        if nums[low] <  nums[high]:
            return nums[low]
        
        mid = (low + high) / 2

        if nums[mid] >= nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]


input= [3, 4, 5, -1, 2, 2.5]
print(findMin(input))
