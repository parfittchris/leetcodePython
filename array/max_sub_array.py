# https: // leetcode.com/problems/maximum-subarray/


def maxSubArray(nums):
    for idx in range(1, len(nums)):
        nums[idx] = max(nums[idx - 1] + nums[idx], nums[idx])

    return max(nums)




input= [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(input))
