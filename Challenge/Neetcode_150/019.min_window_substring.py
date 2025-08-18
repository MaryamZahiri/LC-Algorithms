# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length_s, length_t = len(s), len(t)

        # edge case
        if length_s < length_t: return ""
        if t == s: return t

        freq_t, freq_s = {}, {}
        # build t dictionary
        for char in t: freq_t[char] = 1 + freq_t.get(char, 0)

        # build s dictionary and compare and update window
        left, min_window, window = 0, float("inf"), [-1,-1]
        # keep track of counters
        need, have = length_t, 0
        for right in range(length_s):
            # extend
            freq_s[s[right]] = 1 + freq_s.get(s[right], 0)
            # add counter
            if s[right] in freq_t and freq_t[s[right]] >= freq_s[s[right]]: have += 1
            # meet condition
            while have == need:
                # update window
                if right - left + 1 < min_window: 
                    min_window = right -left + 1                
                    window = [left, right]    
                # shrink
                freq_s[s[left]] -= 1
                # decrement counter
                if s[left] in freq_t and freq_t[s[left]] > freq_s[s[left]]: have -= 1
                left += 1
        left, right = window
        return s[left:right+1]

"""
s: "a"
t: "a"
"a"

s: "aa"
t: "a"
"a"

s: "abab"
t: "aab"
aba

s: "badddcbanc"
         l
           r
b:1
a:0
d:3
c:1
2
6
t: "bac"
banc

aab]
a:2
b:1
t>=s
bba
a:1
b:2
"""