from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, used = set(), set()
        length = len(nums)
        for i in range(length - 2):
            # duplicate
            if nums[i] in used: continue
            used.add(nums[i])

            self.twoSum(nums, i, result)
        return [list(num) for num in result]

    def twoSum(self, nums, i, res):
        seen = set()
        length = len(nums)
        for j in range(i+1, length):
            complement = -nums[i] - nums[j]
            if complement in seen:
                # hashable and immutable
                res.add(tuple(sorted([nums[i], nums[j], complement])))
            seen.add(nums[j])

class Solution2:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            # all possitive 
            if nums[i] > 0: break
            # duplicate
            if i != 0 and nums[i] == nums[i-1]: continue
            # 2 sum
            self.twoSum2(nums, i, result)
        return result
    def twoSum2(self, nums, start, result):
        left, right = start + 1, len(nums) - 1
        while left < right:
            sum_nums = nums[left] + nums[right] + nums[start]
            if sum_nums == 0: 
                result.append([nums[start], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]: 
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
            elif sum_nums > 0: right -= 1
            else: left += 1

class Solution3:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        answer = tuple(sorted([nums[i], nums[j], nums[k]]))
                        if answer not in seen: 
                            seen.add(answer)
                            result.append(list(answer))
        return result
'''
BF: O(n^3) O(1)
[-1,0,1,2,-1,-4]
  i
    j
      k

Sort: O(nlogn + n^2) O(n)
[-1,0,1,2,-1,-4]
[-4,-1,-1,0,1,2]
 i
     l
              r
    
Hash: O(n^2), O(n)
[-1,0,1,2,-1,-4]
  i
           j
hash
-1,0,1,2

[-1,0,1],[-1,2,-1]
'''