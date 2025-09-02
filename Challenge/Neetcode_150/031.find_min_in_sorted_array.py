from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else: 
                left = mid + 1
        return nums[left] 

    def findMinNot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # edge case
        if not right: return nums[0]
        # increasing 
        if nums[0] < nums[-1]: return nums[0]

        while left < right:
            mid = left + (right - left) // 2
            # pivot
            if nums[mid] > nums[mid+1]: return nums[mid+1]
            if nums[mid-1] < nums[mid]: return nums[mid-1]

            # increment
            if numd[0] < nums[mid]: left = mid + 1
            # decrement
            else: right = mid
"""
1
4,5,6,0

BF: O(n), O(1)
3,4,5,1,2
      i
min: 1

Binary Search: O(logn) O(1)
no decreament:
1,2,3,4,5
1<5
->1

4,5,6,7,1,2,3
      l
            r
        m
          +1

pivot:
mid>mid+1
mid-1>mid

increase index 0 < mid -> shift left
decrease index 0 > mid -> shift right

3,4,5,2
    l
      r
    m
      m+1
"""