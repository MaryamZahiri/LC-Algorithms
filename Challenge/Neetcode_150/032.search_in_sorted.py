from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot():
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[right]: right = mid
                else: left = mid + 1
            return left
        def findTarget(left, right):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target: left = mid + 1
                else: right = mid
            return left if nums[left] == target else -1

        pivot = findPivot()
        # left boundry
        if (answer := findTarget(0,pivot-1)) != -1: return answer
        # right boundry
        return findTarget(pivot, len(nums) - 1)
"""
[1], 0 -> -1
[4,5,1,2,3], 0 -> -1
[4,5,1,2,3],1 -> 4

BF: O(n), O(1)
Binary Search: O(logn), O(1)
[4,5,1,2,3],2 -> idx: 2
     l
     r
   m
 pivot = l
 pivot = target -> pivot
 right >= target -> pivot - right
 else -> left - pivot - 1

 -,-,1,2,3
       l   
       r
     m
left
"""