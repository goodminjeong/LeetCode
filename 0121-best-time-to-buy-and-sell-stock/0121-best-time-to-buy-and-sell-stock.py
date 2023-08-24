class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = prices[0], 0, 0

        for i in range(len(prices)-1):
            if prices[i] < buy:
                buy = prices[i]
                
            if buy < prices[i+1]:
                sell = prices[i+1]
                
            if profit < sell - buy:
                profit = sell - buy
                
            sell = 0
            
        return profit