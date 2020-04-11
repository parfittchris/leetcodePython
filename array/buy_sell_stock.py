# https: // leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    if len(prices) == 0:
        return None
        
    profit = 0
    minBuy = prices[0]

    for idx in range(1, len(prices)):
        current = prices[idx] - minBuy

        profit = max(current, profit)
        minBuy = min(minBuy, prices[idx])

    return profit

input = [7, 1, 5, 3, 6, 4]

print(maxProfit(input))
# Output: 5
