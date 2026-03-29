class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if min_cost > prices[i]:
                min_cost = prices[i]
                
            profit = prices[i] - min_cost
            if max_profit < profit:
                max_profit = profit
      
        return max_profit
        