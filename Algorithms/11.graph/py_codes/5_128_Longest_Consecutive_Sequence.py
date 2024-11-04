class Solution:
    def longestConsecutive(self, nums) -> int:
        numNeighbors = set(nums)
        longest = 0

        for n in nums:
            # Check if n is the start of sequence, doesnt have a left neighbor
            if n - 1 not in numNeighbors:
                current_subsequence_length = 0
                # Track the longest length of sequence
                while n + current_subsequence_length in numNeighbors:
                    current_subsequence_length += 1
                longest = max(longest, current_subsequence_length)

        return longest