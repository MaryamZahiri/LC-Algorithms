from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        min_height, max_area = float("inf"), float("-inf")
        while left < right:
            min_height = min(height[left], height[right])
            max_area = max(max_area, (min_height * (right - left)))

            if height[left] < height[right]: left += 1
            else: right -= 1
        return max_area

    def maxArea1(self, height: List[int]) -> int:
        min_height, max_area = float("inf"), float("-inf")
        length = len(height)
        for i in range(length - 1):
            for j in range(i+1, length):
                min_height = min(height[i], height[j])
                max_area = max(max_area, (min_height * (j - i)))
        return max_area 
        
'''
 0 1 2 3 4 5 6 7 8
[1,8,6,2,5,4,8,3,7]
   l
               r
 min
 7
 max area -> index - index
 8 * 7 
 less -> shift
'''