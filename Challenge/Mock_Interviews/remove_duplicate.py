from typing import List 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length_num = len(nums)
        unique_length = 1
        for i in range(1, length_num):
            if nums[i] != nums[i-1]:
                nums[unique_length] = nums[i]
                unique_length += 1
        if unique_length < length_num: nums[unique_length:] = ['_'] * (length_num - unique_length)
        return unique_length
'''
- next index: O(n), O(1)
'''        
'''
[] -> 0
[1] -> 1

[1,  2, 3, 4]
           i-1 i
 unique counts
 4 

[1,  1, 2, 2, 3, 4]
                 i-1 i
 unique counts
 4
 [1,2,3,4,-,-]
'''