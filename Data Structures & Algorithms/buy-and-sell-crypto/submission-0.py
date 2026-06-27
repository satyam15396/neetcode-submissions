class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            currProfit = prices[i] - min_price
            maxProfit = max(currProfit, maxProfit)
            min_price = min(min_price, prices[i])
        return maxProfit