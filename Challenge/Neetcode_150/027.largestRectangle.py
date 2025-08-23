from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        # for only increasing edge case 
        heights.append(0)
        height_len = len(heights)
        
        for cur_idx in range(height_len):
            # shrink if there less height
            while stack and heights[cur_idx] < heights[stack[-1]]:
                pre_height = heights[stack.pop()]
                pre_width = cur_idx if not stack else cur_idx - 1 - stack[-1]
                max_area = max(max_area, pre_height * pre_width)
            # extend
            stack.append(cur_idx)

        return max_area
    """
    T: O(n)
    S: O(n)
    """
"""
monotonic increasing
[1,2,3,4,5,0]
 0 1 2 3 4 5
stack
[1,2,3,4,5]
5
5 - 1 - 3 = 1
4
5 - 1 - 2 = 2
pop height
cur i - 1 - pre stack 
or cur i

[5,4,3,2,1,0]
 0 1 2 3 4 5
stack
[4]
5 
1
cur i
4
2
cur i
"""