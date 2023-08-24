class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = prices[0], 0, 0
 
        for i in range(len(prices)-1):
            if prices[i] < buy:
                buy = prices[i]
                
            if buy < prices[i+1]:
                sell = prices[i+1]
                
            if sell - buy > 0:
                profit += sell - buy
            
            if profit != 0:
                buy = prices[i+1]
                
            sell = 0
            
        return profit