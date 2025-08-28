from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        lower bound
        """
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target: left = mid + 1
            else: right = mid
        if left < len(nums) and nums[left] == target: return left
        else: return -1
    def searchUP(self, nums: List[int], target: int) -> int:
        """
        upper bound
        """
        left, right = 0, len(nums) 
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else: right = mid
        if left > 0 and nums[left - 1] == target: return left - 1
        else: return -1
    def searchNot(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1
            else: right = mid - 1
        # cant find target
        return -1
    """
    T: O(logn)
    S: O(1)
    """
"""
1. BF: O(n)
[-1,0,3,5,9,12], target = 9
          i

2. Binary search
included
 0  1 2 3 4 5
[-1,0,3,5,9,12], target = 9
        l
            r
          m
nums[m] < target -> shift l
-> 4

not included
 0  1 2 3 4 5
[-1,0,3,5,9,12], target = 2
      l
    r
    m
3 > target -> shift r
-1 < target -> shift l
0 < target -> shift l
"""