# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False

        pair = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for char in s:
            # close
            if char in pair:
                if stack and stack[-1] == pair[char]: stack.pop()
                else: return False
            # open
            else:
                stack.append(char)

        return True if not stack else False
        """
        T: O(N) S: O(N)
        """
"""
( -> False
({) -> False
([)] -> F
() -> True
([]) -> T
()[] -> T
"""
"""
() 
OPEN:
stack
[
    (
]

CLOSE:
pop -> (
):(
"""