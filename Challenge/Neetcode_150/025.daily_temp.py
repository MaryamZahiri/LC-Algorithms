# TODO: Optimize space
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_len = len(temperatures)
        stack, result = [], [0] * temp_len

        for idx in range(temp_len):
            # monotonic decreasing stack - if theres increased temp compared to last element in stack
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                start = stack.pop()
                result[start] = idx - start
            # add if it is increasing
            stack.append(idx)
        
        return result
    """
    T: O(n) S: O(n)
    """
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        temp_len, left, right = len(temperatures), 0, 0
        result = [0] * temp_len
        while left < temp_len:
            flag = False    
            while right < temp_len:
                # increased
                if temperatures[left] < temperatures[right]:
                    flag = True
                    result[left] = right - left
                    left += 1
                    right = left
                # decreased
                right += 1
            # not increased 
            if not flag: 
                result[left] = 0
                left += 1
        return result
        """
        T: O(n^2), S: O(1)
        """
"""
BF:
 0   1  2  3  4  5  6  7
[73,74,75,71,69,72,76,73]
                      l
                         r
increased:
r - l
[1, 1, 4, 2, 1, 1, 0, 0]
update l, r
decreased: r ++
end r -> 0

 0   1  2  3  4  5  6  7
[73,74,75,71,69,72,76,73]
                          i
 []
 remove: 
 start: idx - start
 [1,1, 4, 2,1 , 1,0 , 0]
  0 1 2 3   4  5 6 7


[30,40]
 decreasing order monotonic stack
 [30:0] 
 [40:1]

[40,30]
[40:0,30:1]
"""