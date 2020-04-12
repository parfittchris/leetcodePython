# https: // leetcode.com/problems/climbing-stairs/


def climbStairs(n):
    if n < 2:
        return 1

    dp = [None] * n
    dp[0] = 1
    dp[1] = 2

    for idx in range(2, n):
        dp[idx] = dp[idx-1] + dp[idx-2]
    
    return dp[n-1]

input = 3
print(climbStairs(input))