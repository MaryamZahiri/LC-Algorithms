class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length1, length2 = len(s1), len(s2)

        if length1 > length2: return False

        # create dictionary for s1
        counter1 = [0] * 26
        for char in s1: counter1[ord(char) - ord('a')] += 1
        # create dictionary s2 and compare 
        window_len, left = length1, 0
        counter2 = [0] * 26
        for right in range(length2):
            # extend 
            counter2[ord(s2[right]) - ord('a')] += 1
            # shrink
            if right >= window_len:
                left = right - window_len
                counter2[ord(s2[left]) - ord('a')] -= 1
                
            # compare
            if counter1 == counter2: return True
        return False
     
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        counter1 = {}
        for char in s1:
            counter1[char] = 1 + counter1.get(char, 0)
        counter2 = {}
        length, window_len, left = len(s2), len(s1), 0
        for right in range(length):
            # extend
            counter2[s2[right]] = 1 + counter2.get(s2[right], 0)
            # shrink
            if right >= window_len:
                left = right - window_len
                counter2[s2[left]] -= 1
                if counter2[s2[left]] == 0: del counter2[s2[left]]
            if counter1 == counter2: return True
        print(counter1, counter2)
        return False
                
"""
ab
cba
 l
  r
a:1
b:1

c:1
b:1
a:1
"""