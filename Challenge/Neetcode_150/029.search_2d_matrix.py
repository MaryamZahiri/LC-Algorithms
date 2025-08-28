from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        if not ROW: return False
        left, right = 0, ROW * COL - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = mid // COL, mid % COL
            element = matrix[row][col]
            if element == target: return True
            elif element < target: left = mid + 1
            else: right = mid - 1
        return False
        """
        T: O(log(n*m)) S: O(1)
        """
    def searchMatrixNOT(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0]) 
        if matrix[0][0] > target or matrix[-1][-1] < target: return False
        if not ROW: return False

        # find which row
        left, right = 0, ROW - 1
        row = 0
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]: 
                row = mid
                break
            elif target < matrix[mid][0]: right = mid - 1
            else: left = mid + 1

        # binary search to find target
        left, right = 0, COL - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target: return True
            elif matrix[row][mid] < target: left = mid + 1
            else: right = mid - 1
        return False
        """
        T: O(logn + logm) = O(log (n+m))
        """
"""
1. BF: O(N^2), O(1)

2. Binary Search: O(log m + log n)
[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3
  0         1             2
  i
  For row: 0 -> matrix[row][0] <= target <= [row][-1] -> 0 -> return row

  for col -> binary search
  [1,3,5,7]
   l    
         r
     m
    True

3. convert to linear O(n*m)
"""