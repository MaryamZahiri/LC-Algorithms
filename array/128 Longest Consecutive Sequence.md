# LeetCode Problem 128: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## Problem Description

Given an unsorted array of integers nums, return the current_subsequence_length of the longest consecutive elements sequence.

A sequence follows the pattern: ... -> n-2 -> n-1 -> n where n is the current element.

## Solution Approaches

### Hashing/Greedy/Linear Scan Algorithm
Algorithm Pattern:

1. Initialization:
   - Purpose: To prepare the data structure and variables needed for the algorithm.
   - Steps:
        - Create a set numNeighbors from the input list nums. This set is used to quickly check if a number exists in the list, which is an O(1) operation.
        - Initialize longest to 0. This variable will keep track of the length of the longest consecutive sequence found so far.
2. Iterate Through Numbers:
   - Purpose: To identify and measure the length of each consecutive sequence in the input list.
   - Steps:
     - For each number n in the input list nums, perform the following steps:
        - Check if n - 1 is not in numNeighbors. If it is not, then n is the start of a new sequence. It means it doesn't have a left neighbor
        - Initialize current_subsequence_length to 0. This variable will keep track of the length of the current sequence.
        - Enter a while loop, where you keep incrementing current_subsequence_length as long as n + current_subsequence_length is in numNeighbors. This effectively finds the length of the consecutive sequence starting from n.
        - After finding the length of the sequence starting from n, update longest if the current sequence length is greater than the previously found longest sequence.
3. Return Result:
   - Purpose: To provide the final output of the algorithm, which is the length of the longest consecutive sequence found.
   - Steps:
     - Return the length of the longest consecutive sequence found.

## Example Description

<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/8ed51a04-f43a-45b0-b3b0-2125e91c7dab" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/624f814c-5c6c-43cb-89b7-2b2047ce5a33" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/c6d0a13c-6928-403b-b420-b94261a03b8c" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/a689b56c-95e5-4191-9a72-e96c9f809be7" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/bd2c2c96-2bad-4d75-bff1-d475b231e94f" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/53e964c0-0b3b-49e8-a2e1-50acc40cb339" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/b5108eb0-5061-4702-8268-212b705c5a17" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/afa86c0b-dd19-4e06-b4a9-5a48068553e8" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/ddafc335-4731-49d9-8cd0-6aa6f2c747fc" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/5adb5b0b-5046-4c6a-8ffd-8e3a353041a1" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/10ab42fe-f4d5-49dd-bfb3-5f36c544bed4" width=250>
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/84b22723-3bd3-49e6-8e01-232a50b63874" width=250><br />

## Python Code

Input:

```python
# Input
nums = [100,4,200,1,3,2]

# Output: 4

# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
```

## Complexity Analysis

- Time complexity : O(n), where n is the length of the input list nums. This is because the algorithm performs a single pass through the input list.

- Space complexity : O(n), due to the additional space required for the set numNeighbors.