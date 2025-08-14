from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0
        
        left, right = 0, n - 1
        max_left, max_right = 0, 0
        answer = 0
        while left < right:
            # find min of max left or right
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                answer += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                answer += max_right - height[right]
                right -= 1
        return answer
    """
    TC: O(n), SC: O(1)
    """
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0

        max_left_cur, max_right_cur = 0, 0
        max_left, max_right = [0] * n, [0] * n
        # find left and right max
        for i in range(n):
            max_left[i], max_right[n-i-1] = max_left_cur, max_right_cur
            max_left_cur, max_right_cur = max(max_left_cur, height[i]), max(max_right_cur, height[n-i-1])
        
        # find the trap sum
        cur_trap, trap_sum = 0, 0
        for i in range(n):
            cur_trap = max(0, min(max_left[i], max_right[i]) - height[i])
            trap_sum += cur_trap
        return trap_sum
    """
    TC: O(2n), SC: O(2n)
    """
    def trap1(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0
        
        answer, sum_trap = 0, 0
        for i in range(1, n-1):
            max_left, max_right = 0, 0
            for l in range(i):
                max_left = max(max_left, height[l])
            for r in range(n-1, i, -1):
                max_right = max(max_right, height[r])
            answer = max(0, min(max_left, max_right) - height[i])
            sum_trap += answer
        
        return sum_trap
"""
BF:
TC: O(n^2) n.2n
SC: O(1)
[0,1,0,2,1,0,1,3,2,1,2,1]
                     i
 l
                       r
 max left: 
 3
 max right: 
 2
 answer: max(0, min(max left, max right))
 2 - 2
 sum:
 0+1+0+1+2+1+0+0+1+0+0
"""