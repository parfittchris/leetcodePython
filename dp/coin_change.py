# https: // leetcode.com/problems/coin-change/


def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for total in range(1, amount + 1):
            if coin <= total:
                dp[total] = min(dp[total], dp[total - coin] + 1)
    
    if dp[amount] == float("inf"):
        return -1
    else:
        return dp[amount]

coins = [1, 2, 5]
amount = 11


print(coinChange(coins, amount))