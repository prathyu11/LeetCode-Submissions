class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buy = prices[0]

        for price in prices:
            buy = min(buy,price)
            maxprofit = max(maxprofit,price-buy)
        
        return maxprofit


