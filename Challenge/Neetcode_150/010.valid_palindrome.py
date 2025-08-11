class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            # filter remove the characters not alpha numeric
            if not s[left].isalnum(): 
                left +=1 
                continue
            if not s[right].isalnum(): 
                right -= 1
                continue

            # filter lower case
            # not match -> False
            if s[left].lower() != s[right].lower(): return False
            left, right = left + 1, right - 1
        return True
    '''
    dry run:
    aba
      l
    r
    -> True
    '''
    def isPalindrome2(self, s: str) -> bool:
        filtered_s = []
        for char in s:
            if not char.isalnum(): continue

            filtered_s.append(char.lower())
        return filtered_s == filtered_s[::-1]

    def isPalindrome1(self, s: str) -> bool:
        filtered_s = []
        filtered_s = [char.lower() for char in s if char.isalnum()]

        left, right = 0, len(filtered_s) - 1
        while left <= right:
            if filtered_s[left] != filtered_s[right]: return False
        return True

'''
abca -> F
a -> T
aa -> T
aca -> T
l
  r

- filter 
    - remove space
    - lowercase

- reversed: reverse extra space
O(2n) O(2n)

- 2 pointers
O(n) O(1)
'''