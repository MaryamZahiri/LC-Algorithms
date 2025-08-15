from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        length = len(prices)
        for price in prices:
            # no profit and min price is available
            if price < min_price:
                min_price = price
            # profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
    """
    T: O(n) S: O(1)
    """
    def maxProfit1(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for buy in range(n - 1):
            for sell in range(buy + 1, n):
                if prices[sell] - prices[buy] > max_profit:
                    max_profit = prices[sell] - prices[buy]
        return max_profit
    """
    T: O(n^2) S: O(1)
    """
"""
[7,1,5,3,6,4] -> 6 - 1 = 5
[7,6,4,3,1] -> 0

[7,1,5,3,6,4]
     i
       j
 max
 5

one pass
[7,1,5,3,6,4]
   l 
             r 
 buy
 7 > 1
 profit 
 5


"""