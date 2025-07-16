class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        counter = {}
        for i in range(len(s)):
            if s[i] not in counter: counter[s[i]] = 0
            if t[i] not in counter: counter[t[i]] = 0
            counter[s[i]] += 1
            counter[t[i]] -= 1
        
        # check if it is all match
        for char in counter:
            if counter[char] != 0: return False

        return True

    def isAnagramBF(self, s: str, t: str) -> bool:
        # length check
        if len(s) != len(t): return False

        # match check
        matched_list = list(t)
        for s_char in s:
            found = False
            for i in range(len(matched_list)):
                if s_char == matched_list[i]:
                    matched_list[i] = None # mark as used
                    found = True
                    break
            if not found: return found
        
        return found

    def isAnagramSort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
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