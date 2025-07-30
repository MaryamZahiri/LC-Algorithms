class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_s, length_t = len(s), len(t)
        if length_s != length_t: return False
        count_s, count_t = {}, {}
        for i in range(length_s):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_s[t[i]] = -1 + count_s.get(t[i], 0)
        for char in count_s:
            if count_s[char] != 0: return False
        return True
    # O(2n) time complexity, O(n) space complexity

    def isAnagramCompare(self, s: str, t: str) -> bool:
        def count_frequencies(s: str) -> dict: 
            count_fre = {}
            for char in s:
                count_fre[char] = 1 + count_fre.get(char, 0)
            return count_fre
        # edge case: if length is not the same, cannot be anagrams
        if len(s) != len(t): return False
        return count_frequencies(s) == count_frequencies(t)
    # O(3n) time complexity, O(n) space complexity
    # where n is the length of the strings s and t
