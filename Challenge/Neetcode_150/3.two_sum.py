from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            # complement is seen in hash
            if complement in seen: return [seen[complement], i]
            # not exist
            seen[nums[i]] = i
        
        return []

    def twoSumSort(self, nums: List[int], target: int) -> List[int]:
        num_idx = [(num, idx) for idx, num in enumerate(nums)]
        num_idx.sort()
        for i in range(len(num_idx)):
            num, idx = num_idx[i]
            complement = target - num

            left, right = i + 1, len(nums) - 1
            while left <= right:
                mid = left + ((right - left) // 2)
                mid_num, idx2 = num_idx[mid]
                if mid_num == complement:
                    return [idx, idx2]
                elif mid_num < complement:
                        left = mid + 1
                else:
                    right = mid - 1
            return []

    def twoSumBF(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target: return [i, j]
        return []
'''
Sort + BT DR:
1,1,2,3
i
    l
    r
    m
res = []
'''
'''
BF Dry run
1,2,3,1
i     j
'''
'''
1,2 -> 3

3,3 -> 6

BF: O(n^2) O(1)
1,3,4,2
i     j 

Sort: O(NlogN) O(N)
1,1,2,3 -> 2
i
  l     
  r
  m

Hash (i, num): O(N) O(N)
1,2,3,1 -> 2
      i
seen: 
1,2,3
complement:
1
->0,3
'''