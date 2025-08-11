from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        max_streak = 1
        num_set = set(nums)
        for num in num_set:
            # only start from scratch
            if num - 1 in num_set: continue

            # find sequences
            streak = 1
            while num + streak in num_set:
                streak += 1
            max_streak = max(max_streak, streak)

        return max_streak

    def longestConsecutiveSort(self, nums: List[int]) -> int:
        if not nums: return 0

        streak, max_streak = 1, 1
        nums.sort()
        length_num = len(nums)
        for i in range(1, length_num):
            # duplicate
            if nums[i - 1] == nums[i]: continue

            # sequence
            if nums[i - 1] + 1 == nums[i]: streak += 1
            # restart again
            else: streak = 1

            # max so far
            if streak > max_streak:
                max_streak = streak

        return max_streak
    '''
    1,2,3,4,10,11
                  i
    streak:
    2
    max: 
    4
    '''   
    def longestConsecutiveBF(self, nums: List[int]) -> int:
        if not nums: return 0

        max_streak = 1
        for num in nums:
            streak = 1
            if num - 1 in nums: continue

            while num + 1 in nums:
                streak += 1
            max_streak = max(max_streak, streak)
        
        return max_streak
'''
O(n^2) O(1)
[100, 4, 200, 2, 1, 3], 4
                 i 
      j
streak: 1->4

O(nlogn) O(n)
[100, 4, 200, 2, 1, 3], 4
[1,2,3,4,100,200] nlogn
    i-1i
streak: 1->4

Hash: O(n) O(n)
[100, 4, 200, 2, 1, 3], 4
                 i
 100,4,200,2,1,3
 streak: 1->4
'''