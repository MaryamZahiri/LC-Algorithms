from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile/mid)

            # find min hours and min speed
            if hours <= h: right = mid
            else: left = mid + 1
        return left
        """
        T: O(n logm), S: O(1)
        """
        """
        [3,6,7,11], h = 8
        1,2,3,4,5,6,7,8,9,10,11
              l
              r
            m
        3/5 1
        6/5 2
        7/5 2
        11/5 3
        1 + 2 + 2 + 3 = 8

        3/2 6/2 7/2 11/2 high

        3/4 6/4 7/4 11/4 -> 1+2+2+3

        3/3 6/3 7/3 11/3 -> 1+2+3+4
        """
    def minEatingSpeedBF(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            hours = 0
            # calculate hours based on min speed
            for pile in piles:
                hours += ceil(pile/speed)
            if hours <= h:
                return speed
            else:
                speed += 1
    """
    T: O(n.m) S: O(1)
    """
"""
[3,6,7,11], h = 8
speed: 1 - max 11
speed: +1
[3,  6,  7,  11]
             i
Hours
 3/1 6/1 7/1 11/1
 3+6+7+11 > 8

speed: +2
[3, 6, 7, 11]
 i
Hours
 3/2 6/2...
 2+3... > 8

min speed

"""