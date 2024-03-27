# Dynamic Programming

two ways to implement a DP algorithm:
## Bottom-up, also known as tabulation.
A bottom-up implementation's runtime is usually `**faster**`, as iteration does not have the overhead that recursion does.
## Top-down, also known as memoization.
A top-down implementation is usually much `**easier to write**`. This is because with recursion, the `**ordering** of subproblems does not matter`, whereas with tabulation, we need to go through a logical ordering of solving subproblems.