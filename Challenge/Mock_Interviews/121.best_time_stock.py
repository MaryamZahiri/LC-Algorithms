from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case 
        if len(prices) <= 1: return 0
        max_profit, min_price = 0, prices[0]

        # scan prices to find
        for price in prices:
            # no profit
            if price < min_price: min_price = price
            # profit
            elif price - min_price > max_profit: max_profit = price - min_price
        
        return max_profit
    
def main():
    sol = Solution()
    samples = [
        [7,1,2,4,3,6],  # 5 
        [7,6,4,3,1],    # 0
        [1,2,3,4,5],    # 4
        [2,1],          # 0
        [1],            # 0
        [],             # 0
    ]
    for prices in samples:
        print(f"Max profit for {prices} is: {sol.maxProfit(prices)}")

if __name__ == "__main__":
    main()

'''
dry run
[7,2,3,1,6]
           i
 min:1
 max profit:5
'''
'''
BF: O(n^2) O(1)
all possible profits and find max

one scan:
O(n) O(1)
'''
'''
1. [], [1], [3,2,1] -> 0

2. [7,1,2,4,3,6] -> 6 - 1 = 5

7,1,2,4,3,6
          i
no profit: cur - min < 0
min: 
7
1
profit:
0
1-7 < 0
2-1 > 0 -> 1
4-1 > 0 -> 3 max
3-1 > 0 -> 2 x
6-1 > 0 -> 5 max
max update if profit > max profit
'''