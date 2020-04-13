# https: // leetcode.com/problems/longest-increasing-subsequence/


def lengthOfLIS(nums):
    length = 0
    dp = [1] * len(nums)
    
    for i in range(0, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
            
        length = max(length, dp[i])
    
    return length



input = [10, 9, 2, 5, 3, 7, 101, 18]
# input = [10, 9, 2, 5, 3, 4]
print(lengthOfLIS(input))
