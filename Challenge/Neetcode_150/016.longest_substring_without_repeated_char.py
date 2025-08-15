class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_idx = {}
        left = 0
        max_sub_len = 0
        for right, char in enumerate(s):
            # check if there is duplicate
            if char in seen_idx and seen_idx[char] >= left:
                left = seen_idx[char] + 1
            # no duplicate
            seen_idx[char] = right
            # update max length of sub without dup
            max_sub_len = max(max_sub_len, right - left + 1)
        return max_sub_len
    """
    T: O(n) S: O(n)
    """
    """
    abcacbb
       l
         r
    a:3
    b:1
    c:4
    """
    def lengthOfLongestSubstringSet(self, s: str) -> int:
        track_sub = set()
        max_sub_len, length = 0, len(s)
        left = 0
        for right in range(length):
            # check for duplicate
            while s[right] in track_sub:
                track_sub.remove(s[left])
                left += 1
            # no duplicate, add
            track_sub.add(s[right])
            max_sub_len = max(max_sub_len, right - left + 1)
        return max_sub_len
    """
    T: O(n)
    S: O(n)
    """
    def lengthOfLongestSubstringBF(self, s: str) -> int:
        if not len(s): return 0
        
        def check(start, end):
            seen = set()
            for i in range(start, end + 1):
                if s[i] in seen: return False
                seen.add(s[i])
            return True

        max_sub_len = 1
        length = len(s)
        for i in range(length-1):
            for j in range(i+1, length):
                if check(i,j):
                    max_sub_len = max(max_sub_len, j - i + 1)
                else:
                    break
        return max_sub_len
    """
    T: O(n^3) S: O(n)
    """