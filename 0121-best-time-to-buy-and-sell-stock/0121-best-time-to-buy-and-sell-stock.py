class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = prices[0], 0, 0

        for i in range(len(prices)-1):
            buy = min(prices[i], buy)
            sell = max(prices[i+1], buy)
            profit = max(profit, sell - buy)
            sell = 0
            
        return profit