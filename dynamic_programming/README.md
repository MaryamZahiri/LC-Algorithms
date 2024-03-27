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
#### first characteristic - problem will ask for the ***optimum value (maximum or minimum)*** of something, or the ***number of ways*** there are to do something.
- What is the minimum cost of doing...
- What is the maximum profit from...
- How many ways are there to do...
- What is the longest possible...
- Is it possible to reach a certain point...

#### second characteristic
- future "decisions" depend on earlier decisions - This characteristic is what makes a greedy algorithm invalid for a DP problem
> we need to factor in results from ***previous decisions***.