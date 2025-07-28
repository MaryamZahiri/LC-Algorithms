from typing import List 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            # check duplicate
            if num in seen: return True
            # no duplicat
            seen.add(num)
        return False

    def containsDuplicateBF(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]: return True
        return False

    def containsDuplicateSort(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]: return True
        return False
    
    def containsDuplicateCopySort(self, nums: List[int]) -> bool:
        array = nums.copy()
        array.sort()
        for i in range(len(array)):
            if i+1 < len(array) and array[i] == array[i+1]: return True
        return False

    def containsDuplicateSetLength(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
'''
Dry Run:
1,2,2
    i
seen: 1,2
'''
'''
Edge cases: [], [1], [1,2], [1,2,1]
'''
'''
Approach:
1. BF: Time O(N^2), Space O(1)
cons: exceed the time limit
for i 
 for i+1
2. Sort: Time O(N log N + N) -> O(N log N), Space O(N)
cons: in place, modify the array -> copy and sort
1,1,2
i i+1
3. Set: Time O(N), Space O(N)
pros: constant time check
cons: add space
return len(set(nums)) != len(nums)
'''