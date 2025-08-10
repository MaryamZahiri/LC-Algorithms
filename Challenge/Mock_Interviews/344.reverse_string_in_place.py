# 344. Reverse String
# https://leetcode.com/problems/reverse-string/
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    def reverseString1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left, right):
            # base case
            if left >= right: return 

            s[left], s[right] = s[right], s[left]
            reverse(left+1, right-1)

        reverse(0, len(s) - 1)

'''
two pointers: O(n), O(1)
recursion: O(n), O(n)
'''
'''
helo
   l   
 r
olleh
oleh

[] -> []
"a" -> "a" 
'''