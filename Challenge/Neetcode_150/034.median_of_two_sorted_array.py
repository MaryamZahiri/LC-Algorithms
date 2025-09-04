# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1, length2 = len(nums1), len(nums2)
        # go with min length
        if length1 > length2: return self.findMedianSortedArrays(nums2, nums1)

        left, right = 0, length1 - 1
        total = length1+length2
        half = total // 2

        while True:
            mid_a = left + (right - left) // 2
            mid_b = half - (mid_a + 1 + 1)

            # left and right values
            left_a = nums1[mid_a] if mid_a >= 0 else float("-inf")
            right_a = nums1[mid_a+1] if mid_a+1 < length1 else float("inf")
            left_b = nums2[mid_b] if mid_b >= 0 else float("-inf")
            right_b = nums2[mid_b+1] if mid_b+1 < length2 else float("inf")

            # return result if left side < right side
            if left_a <= right_b and left_b <= right_a:
                # odd
                if total % 2: return min(right_a, right_b)
                # even
                else: return (max(left_a, left_b) + min(right_a, right_b)) / 2
            # left a is bigger
            elif left_a > right_b: right = mid_a - 1
            elif left_b > right_a: left = mid_a + 1
        return -1
"""
BF: O(n+m) O(n+m)
odd:
[1,3], [2]
   i      j
 1<2
 1,2,3
 i++,j++
 remaining

Binary search
odd
[1,3], 
[2]
 l
 r
 m
total = 3
half = 3 // 2: 1

left, right: 0, -1
mid a = -1
mid b = 1 - (-1 + 1 + 1) = 0

part a l: -inf || 2 ||
part a r: 2|| inf
part b l: 1 || -inf 
part b r: 3 mid+1

-inf < 3 and 1 < 2
return odd min right -> 2

shrink r-> -1
"""