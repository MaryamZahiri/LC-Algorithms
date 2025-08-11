from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left, right = 0, length - 1
        while left < right:
            complement = numbers[left] + numbers[right]
            if complement == target: return [left+1, right+1]
            elif complement > target: right -= 1
            else: left +=1
        return []
        
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(length):
            complement = target - numbers[i]
            left, right = i+1, length - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == complement: return [i+1, mid+1]
                elif numbers[mid] > complement: right -= 1
                else: left += 1
        return []

    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        length_num = len(numbers)
        for i in range(length_num - 1):
            for j in range(i+1, length_num):
                if numbers[i] + numbers[j] == target: return [i+1,j+1]
        return []
'''
1. BF: O(n^2), O(1)
[2,7,11,15], target = 9
 i
   j
9

2. binary search: O(n logn), O(1)
complement by search for second loop

3. 2 pointer: O(n) O(1)
[2,7,11,15], target = 9
 l
    r
sum:
9
> -> move r
< -> move l
'''