def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    t_list = list(t)
    for char in s:
        found = False
        for i in range(len(t_list)):
            if t_list[i] == char:
                t_list[i] = None  # Mark as used
                found = True
                break
        if not found:
            return False
    return True

# Example usage:
# print(isAnagram("anagram", "nagaram"))  # True
# print(isAnagram("rat", "car"))          # False