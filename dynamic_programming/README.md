# Dynamic Programming
- break it down into smaller subproblems - smaller versions of the original problem that are re-used multiple times
- problem has ***optimal substructure***
- subproblems are also ***overlapping***

## Two ways to implement a DP algorithm:
- Bottom-up, also known as tabulation.
Bottom-up uses iteration
> A bottom-up implementation's runtime is usually ***faster***, as iteration does not have the overhead that recursion does.
- Top-down, also known as memoization.
Top-down uses recursion with cache
> memoizing a result means to store the result of a function call, usually in a hashmap or an array, so that when the same function call is made again, we can simply return the memoized result instead of recalculating the result.
> A top-down implementation is usually much ***easier to write***. This is because with recursion, the ***ordering of subproblems does not matter***, whereas with tabulation, we need to go through a logical ordering of solving subproblems.

## When to Use DP
#### First characteristic 
> problem will ask for the ***optimum value (maximum or minimum)*** of something, or the ***number of ways*** there are to do something.
- What is the minimum cost of doing...
- What is the maximum profit from...
- How many ways are there to do...
- What is the longest possible...
- Is it possible to reach a certain point...

#### Second characteristic
- future "decisions" depend on earlier decisions - This characteristic is what makes a greedy algorithm invalid for a DP problem
> we need to factor in results from ***previous decisions***.
Example: [House Robber](https://leetcode.com/problems/house-robber/description/) | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)

## Strategic Approach to DP
To solve a DP problem, we need to combine 3 things:
1. A function or data structure that will compute/contain the answer to the problem for every given state. dp(i)
2. A recurrence relation to transition between states.
3. Base cases, so that our recurrence relation doesn't go on infinitely.

Top-down, With memoization, our time complexity drops to O(n) - implementations usually use an hashmap dp = {} (cache)
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i <= 2: 
                return i
            if i not in memo:
                # Instead of just returning dp(i - 1) + dp(i - 2), calculate it once and then
                # store the result inside a hashmap to refer to in the future.
                memo[i] = dp(i - 1) + dp(i - 2)
            
            return memo[i]
        
        memo = {}
        return dp(n)
```

Bottom-up - implementations usually use an array dp[i]
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
            
        # An array that represents the answer to the problem for a given state
        dp = [0] * (n + 1)
        dp[1] = 1 # Base cases
        dp[2] = 2 # Base cases
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] # Recurrence relation

        return dp[n]
```