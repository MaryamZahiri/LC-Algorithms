# Dynamic Programming
- break it down into smaller subproblems - smaller versions of the original problem that are re-used multiple times
- problem has ***optimal substructure*** -> we can break complex problems to small piece and solve *sub problems*
- subproblems are also ***overlapping*** -> like fibonacci(n) is fib(n - 1) + fib(n - 2)

## Two ways to implement a DP algorithm:
- Bottom-up, also known as tabulation. (use table/array to store data)
Bottom-up uses iteration
> A bottom-up implementation's runtime is usually ***faster***, as iteration does not have the overhead that recursion does.
- Top-down, also known as memoization.
Top-down uses recursion with cache (memoization)
> memoizing a result means to store the result of a function call, usually in a hashmap or an array, so that when the same function call is made again, we can simply return the memoized result instead of recalculating the result.
> A top-down implementation is usually much ***easier to write***. This is because with recursion, the ***ordering of subproblems does not matter***, whereas with tabulation, we need to go through a logical ordering of solving subproblems.

<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/68f5510f-1527-4724-8097-cee97a68b8a1" width="460"> <img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/a21ef85e-d7a2-43db-92ab-c0c80026a570" width="460">

## When to Use DP
#### First characteristic 
> problem will ask for the ***optimum value (maximum or minimum)*** of something, or the ***number of ways*** there are to do something.
- What is the minimum cost of doing...
- What is the maximum profit from...
- How many ways are there to do... (count steps, ways)
- What is the longest possible...
- Is it possible to reach a certain point...

#### Second characteristic
- future "decisions" depend on earlier decisions - This characteristic is what makes a greedy algorithm invalid for a DP problem
> we need to factor in results from ***previous decisions***.
Example: [House Robber](https://leetcode.com/problems/house-robber/description/) | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)

## LeetCode Problems for Practice
[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/):
- fibonacci -> f(n) = f(n-1) + f(n-2)

[Coin Change](https://leetcode.com/problems/coin-change/description/)

[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)

[Unique Paths](https://leetcode.com/problems/unique-paths/description/)

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

## Strategic Approach to DP
To solve a DP problem, we need to combine 3 things:
1. Objective Function: Problem description. A function or data structure that will compute/contain the answer to the problem for every given state. dp(i) - and
Identify Subproblems: Break down the problem into smaller subproblems, identifying the parameters needed to define each subproblem.
2. Transition Function: Find a function to solve any small to large problems. A recurrence relation to transition between states. Determine how the solution to one subproblem can be used to solve other related subproblems.
3. Implement Memoization or Tabulation: Choose between top-down memoization or bottom-up tabulation based on the problem's characteristics.
4. Handle Base Cases: Ensure that base cases are properly handled to terminate recursion or initialize tabulation. so that our recurrence relation doesn't go on infinitely.

### Examples
*Top-down, With memoization*, our time complexity drops to O(n) - implementations usually use an hashmap dp = {} (cache)

[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/) 
```python
# Objective Function: f(i) is the number of ways to ith stair
# base cases
# F(0) = 1
# F(1) = 1
# F(2) = 2
# recurrence relation: F(n) = F(n-1) + F(n-2)
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i <= 1: 
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

## Practice
### climb stairs: 
- A phone screen interview question
- Optimize Space: O(1)
```python
def climbStairs(n):
    a = 1
    b = 1 
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c
```

Follow up climb stairs:
- 1, 2, 3 staps
- Space Complexity: O(1)
```python
def climbStairs(n):
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]
```
Optimize - Follow up climb stairs:
- 1, 2, 3 staps
```python
def climbStairs(n):
    a = 1
    b = 1
    c = 2
    for i in range(3, n+1):
        d = a + b + c
        a = b
        b = c
        c = d
    return d
```
Follow up - climb stairs (k steps)
- Time Complexity: O(n*k)
- Space Complexity: O(n)
```python
def climbStairs(n, k):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(k + 1):
            if i - j < 0: continue
            
            dp[i] += dp[i - j]

    return dp[n]
```

Optimize Space to k - Follow up - climb stairs (k steps)
```python
# k = 3: [1, 1, 2] : {0, 1, 2}
#        [3, 5, 8] : {3, 4, 5}
def climbStairs(n, k):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(k + 1):
            if i - j < 0: continue
            
            dp[i % k] += dp[(i - j) % k]

    return dp[n % k]
```
Follow up - climb stairs (k steps) + (not red stairs)
```python
def climbStairs(n, k, stairs: bool):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(k + 1):
            if i - j < 0: continue
            if stairs[i-1]: dp[i % k] = 0
            else:
                dp[i % k] += dp[(i - j) % k]

    return dp[n % k]
```
Follow up - climb stairs + return the chipest price
```python
def paidClimbStair(n, p: list):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = p[1]
    for i in range(2,n+1):
        dp[i] = p[i] + min(dp[i -1], dp[i - 2])
    return dp[n]
```
Follow up - climb stairs + return the chipest path
```python
# prices = [0, 2, 4, 1, 3]
# n = 4, idx 0 - 4
# dp = [(0, 0), (2, 0), (4+0, 0), (1+2, idx 1), (3+3, idx 3)]
# output idx = [4, 3, 1, 0]
def paidClimbStairPath(n, p):
    dp = [(0, 0)] * (n+1)
    dp[0] = (0, 0)
    dp[1] = (p[1], 0)
    for i in range(2, n+1):
        dp[i][0] = p[i] + min(dp[i-1][0], dp[i-2][0])
        if dp[i-1][0] < dp[i-2][0]: dp[i][1] = i - 1
        else: dp[i][1] = i - 2
    
    cur = n
    path = [cur]
    for i in range(0,n,-1):
        cur = dp[cur][1]
        path.append(cur)

    # reverse the path
    return path[::-1]
```

### Sum of n nums
```python
# Find sum of first N nums
# Objective function: f(i) is sum of first i elements; Problem description
# Recurrence relation: f(n) = f(n-1) + n

# 1 + 2 + 3 + ...
# F(1) = 1
# F(2) = F(1) + 2
# F(3) = F(2) + 3 = 3 + 3
# F(n) = F(n-1) + n

def sum_nums(nums)
    dp = [0] * (nums + 1)

    for n in nums:
        dp[n] = dp[n-1] + n

    return dp[n]

n = 5
sum_nums(n)
```

### [Unique paths](https://leetcode.com/problems/unique-paths/description/)
- Amazon phone screen question
```python
# Find f(i): how many possible paths are there
# base cases: 
# n = m = 1: f(1, 1) = 1 
# nxm = 2x2: f(2,2) = 2 ways   -------
                            #  |  |  |
                            #  -------
                            #  |  |<^|
                            #  -------
# follow up by bad cells: check if f(i, j-1) or f(i-1, j) == bad cell -> f(i-1, j) = 0 or f(i-1, j) = 0
# follow up by most profitable path: max(f(i, j-1), f(i-1, j)) + p(i,j)
# Transition function: F(i,j) = F(i, j-1) + F(i-1, j) -. think we solved the problem and go to the end of n, m and backward
def uniquePaths(m, n):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    dp[0][0] = 1
    for i in m:
        for j in n:
            if i > 0 and j>0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0: # j = 0
                dp[i][j] = dp[i -1][j]
            elif j > 0: # i = 0
                dp[i][j] = dp[i][j-1]
        return dp[m-1][n-1]
```

follow up - unique path with obstacles
```python
def uniquePaths(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    dp[0][0] = 1
    for i in m:
        for j in n:
            # obstacles
            if grid[i][j]: 
                dp[i][j] = 0
                continue
            if i > 0 and j>0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0: # j = 0
                dp[i][j] = dp[i -1][j]
            elif j > 0: # i = 0
                dp[i][j] = dp[i][j-1]
        return dp[m-1][n-1]
```
follow up - unique path + max profit
```python
# transition function: f(i,j) = max(f(i-1,j), f(i,j-1)) + grid(i,j)
def maxProfitUniquePath(grid):
    row = len(grid)
    col = len(grid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = grid[0][0]
    print(row, col)
    print(dp)
    for i in range(row):
        for j in range(col):
            print(i,j)
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            elif j > 0 and i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
    return dp[row-1][col-1]
```
replacement for +grid
```python
# transition function: f(i,j) = max(f(i-1,j), f(i,j-1)) + grid(i,j)
def maxProfitUniquePath(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(m+1):
        for j in range(n+1):
            dp[i][j] = grid[i][j]
            if i > 0 and j > 0:
                dp[i][j] += max(dp[i-1][j], dp[i][j-1])
            elif i > 0:
                dp[i][j] += dp[i-1][j] 
            elif j > 0:
                dp[i][j] += dp[i][j-1]
    return dp[m-1][n-1]
```
follow up - max Profit path with returning max path idx
- getPath

## Time and Space Complexity
Time Complexity:
- optimize solution that turn exponantioal 2 ^ n to polynominal n ^ 2 or linear time n

Space Complexity:
- Cash n

## Sources: 
[DP](https://www.youtube.com/watch?v=YcrXBDAeTCs&list=PLVrpF4r7WIhTT1hJqZmjP10nxsmrbRvlf&index=9)