# https: // leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    if len(nums) == 0:
        return -1

    lo = 0
    high = len(nums) - 1

    while(lo <= high):
        mid = (lo + high) / 2

        if nums[mid] == target:
            return mid

        if nums[lo] <= nums[mid]:
            if nums[lo] <= target <= nums[mid]:
                high = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                lo = mid + 1
            else:
                high = mid -1

    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 4

print(search(nums, target))
