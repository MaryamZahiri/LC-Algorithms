# https://leetcode.com/problems/generate-parentheses/
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, result = [], []

        def backtrack(open, close):
            # base case
            if open == close == n:
                result.append("".join(paranthese for paranthese in stack))
            # choice 1
            if open < n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()
            # choice 2
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0,0)
        return result
"""
1
(
()

2
(    
()   ((
()(  (())
"""