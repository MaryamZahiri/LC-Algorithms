class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counter = {}
        for i in range(len(s)):
            if not s[i] in counter: counter[s[i]] = 0
            if not t[i] in counter: counter[t[i]] = 0
            counter[s[i]] += 1
            counter[t[i]] -= 1
        for char in counter:
            if counter[char] != 0: return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        for i in range(len(s)):
            if counter[i] != 0: return False
        return True

    def isAnagramSort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    def isAnagramBF(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        list_t = list(t)

        for char in s:
            flag = False
            for i in range(len(list_t)):
                # check if it is matched
                if char == list_t[i]:
                    list_t[i] = None # mark as used
                    flag = True
                    break
            # no match
            if not flag: return False

        return True
        
'''
1. BF: T: O(n^2) S: O(n)
list -> mutable and change the character

2. sorted: T: O(nlogn) S: O(n)
sorted(string) -> list of string

3. hash: T: O(n) S: O(n)
for larger range, hash is better than fixed array (unicode)
'''

# Example usage:
# print(isAnagram("anagram", "nagaram"))  # True
# print(isAnagram("rat", "car"))          # False