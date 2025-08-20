# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isDigit(char):
            return (char.isdigit() or (char.startswith("-") and char[1:].isdigit()))
        def operators(val1, val2, op):
            if op == "+": return val1 + val2
            elif op == "-": return val1 - val2
            elif op == "*": return val1 * val2
            elif op == "/": return int(val1 / val2)
       
        stack = []
        for char in tokens:
            # digit
            if isDigit(char):
                stack.append(int(char))
            # operations and action
            else:
                second = stack.pop()
                first = stack.pop()
                val = operators(first, second, char)
                stack.append(val)
        return stack[-1]
"""
[1,2,+]
 stack
 [1,2]
 + -> second:2 first:1 -> first + second

 [1,2,+,-1,*]
 stack
 [1,2]
 +
 -> second: 2, first: 1 -> 1 + 2 -> 
 [3]
 [3,-1]
 *
 -> second: -1, first: 3: 3 * -1 -> -3
 [-3]
 stack[-1]->-3
"""