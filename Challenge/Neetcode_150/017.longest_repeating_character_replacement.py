class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length, max_window, max_freq = len(s), 0, 0
        if not length: return max_window
        left = 0
        freq_counter = [0] * 26
        for right in range(length):
            # extend window
            freq_counter[ord(s[right]) - ord("A")] += 1 

            max_freq = max(max_freq, freq_counter[ord(s[right]) - ord("A")])

            # shrink window
            if right - left + 1 - max_freq > k:
                freq_counter[ord(s[left]) - ord("A")] -= 1
                left += 1

            # update max_window 
            max_window = max(max_window, right - left + 1)
        return max_window
    """
    T: O(n) S: O(26)
    """
    def characterReplacementDic(self, s: str, k: int) -> int:
        if not len(s): return 0
        counter_char = {s[0]:1}
        max_window = 1
        left = 0
        length = len(s)
        max_val = 1
        for right in range(1, length):
            # extend window
            counter_char[s[right]] = 1 + counter_char.get(s[right], 0)

            max_val = max(max_val, counter_char[s[right]])

            # shrink window
            if right - left + 1 - max_val > k: 
                counter_char[s[left]] -= 1
                left += 1

            # update max window
            max_window = max(max_window, right - left + 1)
        return max_window
    """
    T: O(n) S: O(u)
    """
    """
    abaab, k = 1
     l 
        r
    a:3
    b:1
    window - max val <= k
    2 - 1 = 1
    3 - 2 = 1
    4 - 3 = 1
    """
    def characterReplacementBF(self, s: str, k: int) -> int:
        def check(start, end):
            counter_char = {}
            for i in range(start, end + 1):
                counter_char[s[i]] = 1 + counter_char.get(s[i], 0)
            
            # window length and max value in counter
            max_val = max(counter_char.values())
            if end - start + 1 - max_val > k: return False
            return True

        counter_s = {}
        window_len, length, max_freq = 0, len(s), 0
        for i in range(length - 1):
            for j in range(i+1, length):
                if check(i, j):
                    window_len = max(window_len, j - i + 1)
        return window_len
    """
    T: O(n^3) S: O(n)
    """
"""
abab, k = 2
 i
   j
a:1
b:2
max freq val + k remains = window 
max window - max freq <= k
less -> replace

abaa, k = 1
"""