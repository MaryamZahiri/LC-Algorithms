# https://leetcode.com/problems/sliding-window-maximum/
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k: return [max(nums)]

        queue, result = deque(), []
        left = 0 

        for right, num in enumerate(nums):
            # shrink if queue 0 is less than left
            if queue and queue[0] < left: queue.popleft()

            # keep monotonic decreasing order
            while queue and nums[queue[-1]] < num: queue.pop()

            # extend queue
            queue.append(right)

            # move window and add max to result
            if right - left + 1 == k: 
                result.append(nums[queue[0]])
                left += 1
        
        return result
    """
    T: O(n)
    S: O(n)
    """
    def maxSlidingWindowSet(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k: return [max(nums)]

        window_set = set()
        left, max_num, result = 0, float("-inf"), []
        length_num = len(nums)
        # scan nums
        for right in range(length_num):
            # shrink if it passes window length
            if right - k + 1 > left:
                window_set.remove(nums[left])
                left = right - k + 1

            # extend and find max set
            window_set.add(nums[right])
            max_num = max(window_set)

            if right + 1 >= k: result.append(max_num)
        
        # return result of max for each window
        return result
"""
[1], k = 1 -> [1]

BF: T: O(n.k) S: O(1)
 0 1 2 3 4 5 6 7 8
[1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]
 i
     k
     max 
append max

Sliding Window, set: T: O(n.k) S: O(k)
 0 1 2 3 4 5 6 7 8
[1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]
   l    
         r
 r - l = 4 > k = 3
    l = r - k = 4 - 3
    remove
set
3,-1,-3
max: 3
r >= k: -> append max

sliding window, deque: O(n), O(n)
 0 1 2 3 4 5 6 7 8
[1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]
     l    
           r
shrink left, remove 0

monotonic decreasing
num > first
popleft

deque
[-1:2]

window == k
result[0]
[3]
l += 1
"""