##############################################################
## Top Frequent Meta
##############################################################
from collections import deque, defaultdict, Counter
import random
from typing import List
import heapq
from heapq import heappush, heappop
from math import sqrt
from functools import lru_cache

##############################################################
# 1. 1249. Minimum Remove to Make Valid Parentheses *P
##############################################################
"""
time: O(N)
Space: O(N)
"""
class Meta:
    def minRemoveToMakeValid(self, s):
        stack = []
        invalid = set()

        for idx, char in enumerate(s):
            # close pair
            if char == ")":
                # valid pair in stack
                if stack: stack.pop()
                # no valid
                else: invalid.add(idx)
            # check open pair
            elif char == "(":
                # record in stack
                stack.append(idx)
        
        # remaining stack
        invalid.update(stack)
        
        # generator expression - obj
        return "".join(char for idx, char in enumerate(s) if idx not in invalid)
# TODO: without stack
"""
################################
Input -> Output
s = "lee(t(c)o)de)" -> "lee(t(c)o)de"
s = "lee(t(c)o)de(" -> "lee(t(c)o)de"
s = "))(("          -> ""
"""
"""
################################
Q: 
the only thing is () or lower case?
"""
'''
################################
s1 = "lee(t(c)o)de)"
result = "lee(t(c)o)de"

################################
Valid:
stack ( =   [((]
            []

invalid ) = {end_idx}

################################
s2 = "lll(((("
Invalid:
stack ( =   [((((]
invalid ) = {}
            {((((}
'''

##############################################################
# 2. 408. Valid Word Abbreviation *M
##############################################################
"""
2 pointers:
T: O(n+m)
S: O(1)
"""
class Meta:
    def validWordAbbreviation(self, word: str, abbr: str)->bool:
        # pointers
        word_idx, abbr_idx = 0, 0
        num = 0

        while word_idx < len(word) and abbr_idx < len(abbr):
            # digit
            if abbr[abbr_idx].isdigit():
                # invalid leading 0
                if abbr[abbr_idx] == "0" and not num:
                    return False

                num = num * 10 + int(abbr[abbr_idx])
                abbr_idx += 1
            # no digit
            else:
                if num:
                    # skip num of character
                    word_idx += num
                    num = 0
                # not match
                if word_idx >= len(word) or abbr[abbr_idx] != word[word_idx]:
                    return False
                
                # move pointer
                word_idx += 1
                abbr_idx += 1

        # remaining characters
        if num > 0: word_idx += num

        # processed completely
        return word_idx == len(word) and abbr_idx == len(abbr)
    
"""
################################################
word = "internationalization", abbr = "i12iz4n"

################################################
lead 0 -> False 010
"""

##############################################################
# 3. 56. Merge Intervals
##############################################################
"""
1. Connected component - graph
Time: O(n^2)
Space: O(n^2)

2. Sorting (Timsort-> sort())
Time: O(nlogn)
Space: O(n)
"""
class Meta:
    def merge(self, intervals):
        # sort 
        intervals.sort(key=lambda x:x[0])

        merges = [intervals[0]]

        for start, end in intervals:
            # if merges[0][0] == start and merges[0][1] == end: continue

            pre_end = merges[-1][1]

            # check previous end with current start
            if pre_end >= start:
                merges[-1][1] = max(end, pre_end)
            else:
                merges.append([start, end])

        return merges

"""
return an array of the non-overlapping intervals

[[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
"""

##############################################################
# 4. 227. Basic Calculator II
##############################################################
"""
Time: O(n)
Space: O(n)
- with stack
"""
class Meta:
    def calculate(self, s: str) -> int:
        # initialize record
        stack = []
        num = 0
        last_operator = "+"

        for char in s + "+":
            # check empty space
            if char == " ": continue
            # check if it is digit
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                if last_operator == "+":
                    stack.append(num)
                elif last_operator == "-":
                    stack.append(-num)
                elif last_operator == "*":
                    stack.append(stack.pop() * num)
                elif last_operator == "/":
                    stack.append(int(stack.pop() / num))
                last_operator = char
                num = 0

        return sum(stack) 
    
# TODO: without stack -> space: o(1)
# TODO: other same question
"""
[3 + 2 * 2 * 2] -> 3 + 4 * 2 -> 3 + 8 -> 11
"""

##############################################################
# 5. 314. Binary Tree Vertical Order Traversal *J
##############################################################
"""
1st approach -> BFS + sorted ->
Time: O(nlogn)
return [record_col[key] for key in sorted(record_col.keys())]
"""
"""
Optimized BFS
Time: O(n)
space: O(n)
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode):
        queue = deque([(root, 0)])
        vertical_dic = defaultdict(list)

        max_column = min_column = 0
        while queue:
            cur_node, cur_col = queue.popleft()
            if cur_node:
                # {0: [3, 15], -1: [9], 1: [20], 2: [7]}
                vertical_dic[cur_col].append(cur_node.val)
                min_column = min(min_column, cur_col)
                max_column = max(max_column, cur_col)

                # traverse in tree 
                queue.append((cur_node.left, cur_col - 1))
                queue.append((cur_node.right, cur_col + 1))

        return [vertical_dic[col] for col in range(min_column, max_column + 1)]

"""
root = [3,9,20,null,null,15,7] -> [[9],[3,15],[20],[7]]
                                    -1, 0    , 1,   2
"""
##############################################################
# 6. 1650. Lowest Common Ancestor of a Binary 
##############################################################
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

"""
T: O(N)
S: O(1)
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_copy, q_copy = p, q

        while p_copy != q_copy:
            # move
            p_copy = p_copy.parent if p_copy else q
            q_copy = q_copy.parent if q_copy else p

        return p_copy
###
"""
T: O(N)
S: O(N)
"""
class Meta:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parent_seen = set()

        while p:
            # add all parents seen so far
            parent_seen.add(p)

            # move to next node
            p = p.parent

        while q:
            # check if parent already seen
            if q in parent_seen:
                return q

            # move to next parent
            q = q.parent

        return None
"""
all parent include itself, add to set
check if there is any common
"""
####

"""
Q:
input: p, q and not root
in class Node, obj.parent
node: unique
p, q exist
"""
"""
2 iteration to fill the gap
root parent is None -> swap
"""
"""
Example:
[3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 -> parent 3
"""
##############################################################
# 7. 339. Nested List Weight Sum *M
##############################################################
class NestedInteger:
    def __init__(self, val = None):
        self.val = val if val else []
    def isInteger(self):
        return isinstance(self.val, int)
    def getInteger(self):
        return self.val
    def getList(self):
        return self.val
"""
Time: O(N) 
N: total number of integer and list - traverse all element exactly once
Space: O(D)
D: max depth of nesting
"""
class Meta:
    def depthSum(self, nestedList:'NestedInteger'):
        def dfs(nestedList, depth):
            total = 0

            for element in nestedList:
                # TODO: function for isInteger
                # check if it is integer
                if element.isInteger():
                    # TODO: function for getInteger
                    total += element.getInteger() * depth
                # it is list
                else:
                    total += dfs(element.getList(), depth + 1)

            return total

        return dfs(nestedList, 1)
"""
[[1,1],2,[1,1]] - > 10 
2 * 1 + 2 * 1 + 1 * 2 + 2 * 1 + 2 * 1 = 10
"""
##############################################################
# 8. 528. Random Pick with Weight
##############################################################
"""
Time: 
- construct prefix sum: O(N)
- pickIdx O(logN)
Space: 
- O(N)
- O(1)
"""
class Meta:
    def __init__(self, w: List[int]):
        self.prefix_sum = []

        total = 0
        for weight in w:
            total += weight 
            self.prefix_sum.append(total)

        self.total = total

    def pickIndex(self) -> int:
        # random guess
        target = random.uniform(0,self.total)

        # binary search
        left, right = 0, len(self.prefix_sum)
        while left < right:
            mid = left + (right - left) // 2
            mid_range = self.prefix_sum[mid]

            if target > mid_range:
                # shift left
                left = mid + 1
            else:
                right = mid
        # the start of interval range
        return left
"""
W   [1,3,4] -> [1,3,3,3,4,4,4,4] -> range interval [1,1+3,4+4] -> prefix
IDX [0,1,2] -> 1/8, 3/8, 4/8     ->              [0-1,1-4,4-8] -> random target
"""
##############################################################
# 9. 215. Kth Largest Element in an Array
##############################################################
"""
Time: O(nlogk)
Space: O(k)
"""
class Meta:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            # keep the length of heap in length of k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

"""
nums = [3,2,1,5,6,4], k = 2 -> output = 5
"""
####
"""
Time: O(nlogn)
Space: O(n)
"""
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]
    
# TODO: quick select - O(n)
##############################################################
# 10. 680. Valid Palindrome II
##############################################################
"""
2 pointers:

Time: O(n) 
- isPalindrome proportional of the main run (it is continuous)
Space: O(1)
- for two-pointer logic 
"""
class Meta:
    def validPalindrome(self, s: str) -> bool:
        # two pointers
        def isPalindrome(string, left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            # check if we can skip unmatched and check the next characters from left or right side
            if s[left] != s[right]:
                return isPalindrome(s, left + 1, right) or isPalindrome(s, left, right - 1)
            # shift pointers
            left += 1
            right -= 1

        # It is a palindrome 
        return True
    """
    Time: O(n)
    - The recursion depth is small, as k=1, making the algorithm linear in practice
    Space: O(1 to n)
    - for two-pointer logic and constant recursion depth for k=1
    """
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right, counter):
            while left < right:
                # mismatch
                if s[left] != s[right]:
                    # at most one skip
                    if counter <= 0: return False
                    return isPalindrome(left + 1, right, counter - 1) or isPalindrome(left, right - 1, counter - 1)
                left, right = left + 1, right - 1
            
            # match 
            return True

        return isPalindrome(0, len(s) - 1, 1)
    
    """
    2 pointers:

    Time: O(n) 
    Space: O(1 or n)
    - for two-pointer logic and slicing is temprary 
    - if consider this temprary, O(n)
    """
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right:
                # mismatch
                if s[left] != s[right]:
                    return s[left + 1: right + 1] == s[left + 1: right + 1][::-1] or s[left:right] == s[left:right][::-1]
                left, right = left + 1, right - 1
            
            # match 
            return True

        return isPalindrome(0, len(s) - 1)
    
##############################################################
# 11. 1570. Dot Product of Two Sparse Vectors *F
##############################################################
"""
Hashtable:
Time: O(n), O(L)
Space: O(L), O(1)
"""
class SparseVector:

    def __init__(self, nums: List[int]):
        # non-zero elements including indices
        self.sparse = {i:value for i,value in enumerate(nums) if value != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        sparse1 = self.sparse 
        sparse2 = vec.sparse

        # iterate 
        for idx in sparse1.keys():
            if idx in sparse2:
                total += sparse1[idx] * sparse2[idx]
        
        return total
    
"""
sparse vector -> 1d array with mostly zero elements
"""
"""
Non-efficient Array
Time: O(n)
Space: O(1)
"""
class SparseVector:
    def __init__(self, nums):
        self.array = nums

    def dotProduct(self, vec):
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result

# TODO: Follow up: What if only one of the vectors is sparse?
##############################################################
# 12. 560. Subarray Sum Equals K
##############################################################
"""
T: O(n)
S: O(n)
prefix sum + (hashmap) dictionary of counter to check if prefix sum is seen so far!
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # init
        prefix_sum = 0
        counter = 0
        prefix_counter = {0: 1}

        for num in nums:
            prefix_sum += num

            # check if the difference exist in dictionary -> subtract ->> subarray
            if prefix_sum - k in prefix_counter:
                counter += prefix_counter[prefix_sum - k]

            # update and add to dictionary
            prefix_counter[prefix_sum] = 1 + prefix_counter.get(prefix_sum, 0)

        return counter
"""
Inefficient: Brute Force
Time: O(n^3)
"""

"""
Input: nums = [1,2,3], k = 3
Output: 2 (counter of subarrays)
"""
"""
Q:
subarray is a contiguous non-empty?
subarray length 1?
count subarray?
"""
"""
current + pre_sum -> pre_sum - k = removable sub array
1, 2, 3 -> 
1,2 -> 3 -3 = 0 -> counter += 1
3 -> 3 + 3 - 3 = 3 complete -> counter += dictionary
{
    0:1,
    3:1,
    6:1
}

1,1,1,2,3 , k = 3
{
    0:1
    1:1,
    2:1,
    3:1, -> 3 - 3 = 0 is previous sum to remove -> add to counter
    5:1, -> 5 - 3 = 2 is previous sum to remove -> add to counter -> it means: total sum - previous sum = 5 - 2 = 3 = k
    8:1  -> 8 - 3 = 5 is previous sum to remove -> add to counter 
}
"""
##############################################################
# 13. 162. Find Peak Element *F (Vallay - local min)
##############################################################
"""
Time: O(logn)
Space: O(1)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # compare with next element
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left
"""
Time: O(logn)
Space: O(logn)
"""
class Meta:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        return self.search(nums, left, right)

    def search(self, nums, left, right):
        # base case 
        if left >= right: return left

        mid = (right + left) // 2

        if nums[mid] < nums[mid+1]:
            return self.search(nums, mid+1, right)
        return self.search(nums, left, mid)
"""
Linear scan
Time: O(n)
Space: O(1)
"""
class Solution:
    def findPeakElement(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

"""
return the index of max of neighbors 
"""
"""
Input: nums = [1,2,3,1]
Output: 2

nums = [1,2,3]
output: 2

multi peak
Input: nums = [1,2,1,3,5,6,4]
Output: 5 or 1

"""
"""
Q:
multiple peak?
outside the array range? (In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.)
empty? no
unique? nums[i] != nums[i + 1] for all valid i
"""
##############################################################
# 14. 347. Top K Frequent Elements
##############################################################
"""
Time: O(n + m.logk) 
- n Counter
- m unique element in dictionary
- log k heappush and heappop operations in heap
Space: O(m + k)
- m counter 
- k heap  
"""
class Meta:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        # Count frequency - dic
        count_frequency = Counter(nums)

        # min heap
        min_heap = []
        # iterate
        for num, count in count_frequency.items():
            # add num to heap
            heappush(min_heap, (count, num))
            # pop if it pass the window length k
            if k < len(min_heap):
                # remove min from priority queue
                heappop(min_heap)

        # if we need to extract top k element
        return [num for _, num in min_heap]
"""
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Input: nums = [-1,-1], k = 1
# Output: [-1]
"""
"""
    Heap:
    - By removing the smallest frequency element, we ensure the heap always contains the k most frequent elements.
    - heapq does not guarantee a sorted order in the entire structure
    - while heapq ensures the root is the smallest element, the rest of the elements may not be in strict sorted order. (parent ≤ children)
"""
"""
Bucket Sort
Time: O(n) count freq + filling bucket
- O(n+k) collect top k
Space: O(n) freq map & bucket
"""
class Meta:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        freq = Counter(nums)
        
        # Step 2: Create a bucket for frequency (index = frequency)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
        
        # Step 3: Extract the top k frequent elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # Start from the most frequent
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
"""
# bucket = [
#     [],        # index 0 (no element appears 0 times)
#     [3],       # index 1 (3 appears once)
#     [2],       # index 2 (2 appears twice)
#     [1],       # index 3 (1 appears three times)
# ]
# Start from the highest frequency bucket (index = 3) and collect elements.
# result = []
# result.append(1)  # result = [1]
# result.append(2)  # result = [1, 2]
"""

"""
T: O(mlogm)
S: O(n)
"""
class Meta:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)

        sorted_freq = [key for key, _ in sorted(freq_count.items(), key= lambda x: x[1], reverse=True)]

        return sorted_freq[:k]
##############################################################
# 15. 71. Simplify Path
##############################################################
"""
Time: O(n) = O(n)
- split()
- process each component ""
Space: O(2n) = O(n)
- stack
- split component
"""
class Solution:
    def simplifyPath(self, s: str)-> str:
        stack = []
        
        for char in s.split("/"):
            if char == "..":
                if stack: stack.pop()
            elif char and char != ".":
                stack.append(char)
        return "/" + "/".join(stack) 
"""
without split
Time: O(n)
Space: O(n)
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        # record in stack to undo when . or ..
        stack = []
        cur_directory = ""

        for char in path + "/":
            # Start a directory
            if char == "/":
                # Remove last directory if cur ..
                if cur_directory == "..":
                    if stack: stack.pop()
                # Add directory if there is no period
                elif cur_directory != "" and cur_directory != ".": 
                    # Ignore as it is current directory
                    stack.append(cur_directory)
                # Reset current directory
                cur_directory = ""
            else:
                # Add to current directory
                cur_directory += char

        # return current directories in stack, adding /
        return "/" + "/".join(stack)
                
"""
path = "////./../2/_/...."
path = "////./../"
path = "//home/meta/.." -> /home
        "/../"

s.split("/") -> ["", "home", ""] -> check empty or if char
"""
"""
Q:
unix path inside? letters, digits, period '.', slash '/' or '_'.
valid unix path, empty?
"""
##############################################################
# 16. 50. Pow(x, n) *F
##############################################################
"""
iteration:
Time: O(logn)
- reduce n by half
Space: O(1)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # edge case
        if n == 0: return 1

        if n < 0: 
            n = -1 * n
            x = 1 / x 

        result = 1
        while n:
            # odd power
            if n % 2 != 0:
                n -= 1
                result *= x 
            # even
            x *= x
            n /= 2
        
        return result
"""
recursive
Time: O(logn)
Space: O(logn)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.pow(x,n)

    def pow(self, x, n):
        # base case - 2^0
        if n == 0: return 1

        # edge case - negative
        if n < 0: return 1 / self.pow(x, -1 * n)

        # odd power
        if n % 2 != 0: return x * self.pow(x * x, (n - 1)/2)
        # even power
        else: return self.pow(x * x, n / 2)
"""
2^5 -> 2*f(4)^2 -> 2 * f(4*4) * 2^0 -> 2 * 16 
2^2 -> 2*2 = 4
2^3 -> 2 *f(4, 1) * 2^0 
Input: x = 2.00000, n = -2
Output: 0.25000
"""
"""
edge case:
negative n
even n
odd n
x 0?
"""
##############################################################
# 17. 670. Maximum Swap *FF
##############################################################
"""
Approach 1: Brute Force
    for i in range(n):
        for j in range(i + 1, n):
Time: O(n^2)
Space: O(n)
"""
"""
Time: O(10n)
- convert string O(n)
- map O(n)
- traverse and comparison O(9n)
- convert to int O(n)
Space: O(n)
"""
class Meta:
    def maximumSwap(self, num: int) -> int:
        # conversion 
        num_list = list(str(num))

        # dictionary value: index - occurance of digits
        num_dic = {int(value): idx for idx, value in enumerate(num_list)}

        # iteration
        # Traverse the string to find the first digit that can be swapped with a larger one
        for idx, cur_digit in enumerate(num_list):
            for digit in range(9, int(cur_digit), -1):
                # swap, check if is there any digit greater than num
                if num_dic.get(digit, -1):
                    num_list[idx], num_list[num_dic[digit]] = num_list[num_dic[digit]], num_list[idx]
                    return int("".join(num_list))
        
        return num
##############################################################
# 18. 236. Lowest Common Ancestor of a Binary Tree
##############################################################
"""
Time: O(n)
- visit all nodes at worst
Space: O(n)
- recursion call stack
"""
class Meta:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            # base case - empty tree
            if not node or node == p or node == q: return node

            # traverse
            left = dfs(node.left)
            right = dfs(node.right)

            return node if left and right else left if left else right

        return dfs(root)
"""
Q:
p,q exists
node unique
"""
##############################################################
# 19. 921. Minimum Add to Make Parentheses Valid
##############################################################
"""
Open Bracket Counter
Time: O(n)
Space: O(1)
"""
class Meta:
    def minAddToMakeValid(self, s: str) -> int:
        track_pair, invalid_pair = 0, 0

        for char in s:
            # close
            if char == ")":
                if track_pair > 0: track_pair -= 1
                else: invalid_pair += 1
            # open
            else:
                track_pair += 1

        return track_pair + invalid_pair
"""
s = "())(" -> counter = 2
"""
##############################################################
# 20. 125. Valid Palindrome
##############################################################
"""
compare with reverse
Time: O(n)
- filter isalnum()
- lower()
- list and reverse
- compare 
Space: O(n)
"""
"""
2 pointer
Time: O(n)
- at most once visit
Space: O(n)
"""
class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum(): 
                left += 1
                continue
            if not s[right].isalnum(): 
                right -= 1
                continue

            # mismathch
            if s[left].lower() != s[right].lower(): return False

            left += 1
            right -= 1

        return True
"""
empty? space? alpha, num? lower?
"""
"""
Input: s = "A man, a plan, a canal: Panama"
Output: true
"""
##############################################################
# 21. 138. Copy List with Random Pointer @
##############################################################
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
Time: O(n)
Space: O(n)
- recursive call stack
- dictionary
"""
# TODO: class Node
class Node:
    def __init__(self, node, next = None, random = None):
        self.node = node
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.seen = {}

    def copyRandomList(self, head: Node)->Node:
        # base case 
        if not head: return None

        # return cache
        if head in self.seen:
            return self.seen[head]

        copy = Node(head.val, None, None)

        # mark as seen
        self.seen[head] = copy

        # update
        copy.next = self.copyRandomList(head.next)
        copy.random = self.copyRandomList(head.random)

        return copy
"""
[[7,null],[13,0]]
7.random = null
13.random = 0
----------------------
in clone.next call -> add all in dictionary
in clone.random call -> all are in dictionary and we return clone
----------------------
"""

"""
Time: O(n)
Space: O(1)
"""
class Meta:
    def copyRandomList(self, head: 'Node')->'Node':
        if not head: return None

        # 1->1'->2->2'->3->3'
        def createClone(head):
            current = head
            while current:
                # create Node
                copy = Node(current.val)
                nxt = current.next
                current.next = copy
                copy.next = nxt
                # move to next node
                current = copy.next

        # 1'.random = 3'
        # current.next is our clone in previous function
        def assignRandomClone(head):
            current = head
            while current:
                # check if random exist
                if current.random:
                    current.next.random = current.random.next

                # move node - skip copy nodes -> current.next is copy
                current = current.next.next

        # 1->1'->2->2'
        # 1'->2'->3'
        def seperateClone(head):
            original = head
            # clone is next of head
            clone_head = head.next
            clone_tail = clone_head
            while original:
                # original
                original.next = clone_tail.next
                # move to next
                original = original.next

                # clone clone_tail.next*
                if clone_tail.next:
                    clone_tail.next = clone_tail.next.next
                    # move to next in clone
                    clone_tail = clone_tail.next

            return clone_head

        createClone(head)
        assignRandomClone(head)
        clone = seperateClone(head)

        return clone
    
"""
[1,3]->[2,1]->[3->null]
1.random = 3
2.random = 1
3.random = null
--------------------------------
original + clone
1->1'->2->2'->3->3'

assign random pointer to clone
1'.random = 3'
2'.random = 1'
3'.random = null

clone.random = original.random.next


seperating original from clone
1->2->3
1'->2'->3'
"""
##############################################################
# 22. 938. Range Sum of BST
##############################################################
"""
DFS - recursive - optimized by bound right left conditions
T: O(n)
S: O(H) balanced
   O(n) skewed
"""
class Meta:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node, path_sum):
            if not node: return 0

            path_sum = 0

            if low <= node.val <= high: 
                path_sum += node.val

            if low < node.val:
                path_sum += dfs(node.left, path_sum)
            if high > node.val:
                path_sum += dfs(node.right, path_sum)

            return path_sum

        return dfs(root, 0)
"""
DFS - stack - optimize
T: O(n)
S: O(n) at worst
"""
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root: return 0

        stack = [root]
        total = 0

        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    total += node.val

                if low < node.val:
                    if node.left: stack.append(node.left)
                if node.val < high:
                    if node.right: stack.append(node.right)
        return total
##############################################################
# 23. 1091. Shortest Path in Binary Matrix
##############################################################
"""
BFS - queue - 
Time: O(n^2)
Space: O(n^2)
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        # edge case - block 1
        if grid[0][0] == 1 or grid[ROW - 1][COL - 1] == 1: return -1

        queue = deque([(0,0,1)])
        # visited
        grid[0][0] = 1
        direction = [
            # horisontal - virtical
            (0,1),(0,-1),(1,0),(-1,0),
            # diagnal
            (1,1),(1,-1),(-1,1),(-1,-1)
        ]


        while queue:
            cur_row, cur_col, path_len = queue.popleft()
            # check if it is reach last cell
            if cur_row == ROW - 1 and cur_col == COL - 1: return path_len

            for row_dir, col_dir in direction:
                new_row, new_col = cur_row + row_dir, cur_col + col_dir

                
                # check out of bound 
                if (not (0 <= new_row < ROW) 
                    or not (0 <= new_col < COL)
                    or grid[new_row][new_col] == 1):
                    continue

                grid[new_row][new_col] = 1
                # add to queue
                queue.append((new_row, new_col, path_len + 1))

        return -1
    
"""
why shortest path
BFS explores all nodes at the current "depth" (or distance) before moving to the next level.
As a result, the first time the bottom-right cell is reached, it is guaranteed to be with the shortest path length.
"""
"""
advanced - priority queue - heapq
"""
##############################################################
# 24. 1762. Buildings With an Ocean View
##############################################################
"""
Monotonic stack - decreasing
Time: O(n)
- push, pop at most once O(1)
Space: O(n)
- result O(1) or O(n)
"""
class Meta:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for idx in range(len(heights)):
            # current height is blocked >
            while stack and heights[stack[-1]] <= heights[idx]:
                # there is no view
                stack.pop()
            # we have view
            stack.append(idx)
        
        return stack
"""
good: [4,2,3] -> [4,3] -> [0,2]
bad: [2,2,2,2] -> [3]
"""
"""
Improve space:
T: O(n)
S: O(1)
"""
class Meta:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = []
        max_height = float('-inf')  # Initialize the maximum height to negative infinity
        
        # Iterate from right to left
        for idx in range(n - 1, -1, -1):
            if heights[idx] > max_height:
                result.append(idx)  # Add index to the result if it has an unobstructed view
                max_height = heights[idx]  # Update the maximum height encountered
        
        return result[::-1]  # Reverse the result to maintain ascending order of indices
"""
bad example: 3,2,1,4 -> 4 -> 3
good example: 4,3,2,1 -> all
"""
##############################################################
# 25. 636. Exclusive Time of Functions (@)
##############################################################
"""
LIFO - stack id - nested function
Time: O(L) log
Space: O(n) id
"""

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # init to record id -> index
        stack = []
        executive_time = [0] * n
        pre_time = 0

        for log in logs:
            # parse
            task_id, status, timestamp = log.split(":")
            task_id, timestamp = int(task_id), int(timestamp)

            # check status
            if status == "start":
                if stack:
                    executive_time[stack[-1]] += timestamp - pre_time
                stack.append(task_id)
                pre_time = timestamp
            else:
                executive_time[stack.pop()] += timestamp - pre_time + 1
                pre_time = timestamp + 1

        return executive_time
"""
Nested Function Calls: 
(similar to open and close parantheses (()) -> start0 start1 end1 end2)
Functions can start and end in a nested manner, e.g., f1 starts, then f2 starts, f2 ends, and finally f1 ends. This is like a Last-In-First-Out (LIFO) process, where the most recently started function is the first to end.

0-2 -> 0: start 2 - 0
2-5 -> 1: end   (5 - 2) + 1
5-6 -> 0: end   6 + 1 - (5 + 1)

start -> pre = time
end   -> pre = time + 1
"""
##############################################################
# 26. 346. Moving Average from Data Stream
##############################################################
class MovingAverage:
    """
    Time: O(1)
    Space: O(k)
    """
    def __init__(self, size: int):
        self.size = size
        self.total = 0
        self.queue = deque([])
    def next(self, value: int) -> float:
        self.queue.append(value)
        self.total += value

        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
            
        ave_total = self.total / len(self.queue)
        return ave_total

##############################################################
# 27. 973. K Closest Points to Origin
##############################################################
class Solution:
    """
    [[0,3], [2,0]] k=1 -> [2,0] <= -3 < -2 remove -3
    Time: O(nlogk)
    Space: O(k)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            distance = sqrt(x**2 + y**2)
            
            heappush(max_heap, (-distance, [x,y]))

            # check and keep the length of heap by k
            if len(max_heap) > k:
                # remove large distance
                heappop(max_heap)

        return [coordinate for _, coordinate in max_heap]
    
"""
Sort
T: nlogn
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the list with a custom comparator function
        points.sort(key=self.squared_distance)
        
        # Return the first k elements of the sorted list
        return points[:k]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2
    
# TODO: Quick select
##############################################################
# 28. 426. Convert Binary Search Tree to Sorted Doubly Linked List - in place
##############################################################
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Meta:
    def __init__(self):
        self.first = None
        self.last = None

    def treeToDoublyList(self, root: TreeNode)-> TreeNode:
        if not root: return None

        self.inorder(root)

        # circular to link first and last # circular manner # ->1...3->
        self.first.left = self.last
        self.last.right = self.first

        # head of in place
        return self.first

    def inorder(self, node):
        # base case 
        if not node: return 

        # left 
        self.inorder(node.left)

        # link node in place
        # 1 <-> 2 <-> 3
        if self.last:
            # link 
            self.last.right = node
            node.left = self.last
        else:
            # update first
            self.first = node

        # move last node
        self.last = node

        # right
        self.inorder(node.right)
    """
    root = [4,2,5,1,3] -> [1,2,3,4,5]
         4
       2    5
    1     3

    Inorder tree: left node right
    first, move last
    Circular

    persist changes in class
    """

##############################################################
# 29. 199. Binary Tree Right Side View
##############################################################
"""
BFS
time: O(N) 
- visit once
space: O(D) diameter
- N/2 last level
"""
class Solution:
    def rightSideView(self, root):
        if not root: return []
        
        queue = deque([root])
        level_result = []

        while queue:
            right_side_view = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    right_side_view = node.val # 1: 1 , 2: 2, 3

                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            if right_side_view: level_result.append(right_side_view) # [1,3]
# TODO: DFS
"""
Time: O(N)
Space: O(H) 
- at worst: O(N)
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        rightside = []

        def helper(node: TreeNode, level: int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside
##############################################################
# 30. 987. Vertical Order Traversal of a Binary Tree
##############################################################
"""
time: O(n + kmlogm)
space: O(n + m)
"""
class Solution:
    def verticalTraversal(self, root):
        queue = deque([(0,0,root)])
        vertical_order = defaultdict(list)
        max_col, min_col = float("-inf"), float("inf")

        while queue:
            for _ in range(len(queue)):
                col, row, node = queue.popleft()
                if node:
                    vertical_order[col].append((row, node.val)) # {0:[(0,3),(2,15)],-1:[(1,9)], 1:[(1,20)]}

                    max_col = max(max_col, col)
                    min_col = min(min_col, col)

                    # traverse
                    if node.left: queue.append((col - 1, row + 1, node.left))
                    if node.right: queue.append((col + 1, row + 1, node.right))

        # sort: in range of col
        result = []
        for col in range(min_col, max_col + 1):
            # sort first by row, then by value for same row
            nodes = sorted(vertical_order[col], key= lambda x:(x[0],x[1]))
            result.append([val for _, val in nodes])
        # result = [[val for _, val in sorted(vertical_order[col], key=lambda x: (x[0],x[1]))] for col in range(min_col, max_col+1)]
        return result
##############################################################
# 31. 791. Custom Sort String
##############################################################
class Solution:
    """
    Time: O(n+m)
    Space: O(n)
    """
    def customSortString(self, order: str, s: str) -> str:
        # freq counter
        freq_s = Counter(s)
        record = []

        # sort based on order
        for char in order:
            # check char exists
            if char in freq_s:
                record.append(char * freq_s[char])
                del freq_s[char]

        # add remaining in s
        for char, counter in freq_s.items():
            record.append(char * counter)

        return "".join(record)
"""
    sort 
    Time: O(logn)

    Brute force:
    for order
        for s
    Time: O(n^2)
    --------------------------------
    order = "cba", unique, keep order 
    s = "abcd"  -> sorted based on order

    frequency counter
"""

##############################################################
# 32. 65. Valid Number
##############################################################
import re
"""
T: O(n) linear through string
S: O(1) or O(n) 
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        # regex pattern
        rSign = r'[+-]?'
        rDec = r'\d+\.\d*|\d*\.\d+'
        rInt = r'\d+'
        eE = r'([eE][+-]?\d+)?'
        pattern = f"{rSign}({rDec}|{rInt}){eE}"

        return re.fullmatch(pattern, s) is not None
"""
pattern:
[sign][intger or decimal.][eE]
"""
"""
Parse
T: O(n) linear through string
S: O(1) 
"""
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_decimal = seen_exponent = False

        for idx, char in enumerate(s):
            # digit
            if char.isdigit():
                seen_digit = True
            # +-
            elif char in "+-":
                # only the first character
                # or after e E
                if idx > 0 and s[idx - 1] not in "eE":
                    return False
            # exponent
            elif char in "eE":
                # digit must followed by e
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # It must followed by digit
                seen_digit = False
            # decimal
            elif char == ".":
                if seen_decimal or seen_exponent:
                    return False
                seen_decimal = True
            else:
                # any other character
                return False

        # seen at least one digit
        return seen_digit
"""
pattern:
[sign][intger or decimal.][eE]

'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
^start
$end
[] group
\d+ 1 or more digit
\d* 0 or 1
?   0 or 1 
"""

##############################################################
# 33. 708. Insert into a Sorted Circular Linked List
##############################################################
"""
Time: O(N)
Space: O(1)
"""
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head: 
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

        prev, cur = head, head.next
        toInsert = False
        
        while True:
            # handle the commnon use case -> ->3->4->1->(2')-> # 3->4->5'->6
            if prev.val <= insertVal <= cur.val:
                toInsert = True

            # handle circular manner -> ->3->4->(0')->1-> or ->3->4->(5')->1->
            elif prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    toInsert = True
            

            # already found the position to insert
            if toInsert:
                new_node = Node(insertVal, cur)
                prev.next = new_node
                return head

            # move
            prev, cur = cur, cur.next

            # circular loop
            if prev == head:
                break

        # None of edge case (no result till now) - current, previous node and head are equal -> ->1->(0') or ->3->(10')->3->3->
        prev.next = Node(insertVal, cur)
        return head
    """
    ->
    ->1->

    ->1->
    ->1->0->

    ->3->4->1->
    ->3->4->1->(2')->

    ->3->4->(0')->1-> or ->3->4->(5')->1->

    ->3->4->(0')->1-> or ->3->4->(5')->1->
    """
##############################################################
# 34. 249. Group Shifted Strings
##############################################################
class Solution:
    """
    Time: O(n.k)
    Space: O(n.k)
    """
    def groupStrings(self, strings: List[str])-> List[List[str]]:
        # pattern
        def getPattern(s):
            pattern = []

            for idx in range(1, len(s)): # O(k)
                # difference of shifted backward or forward + modulo to handle wrap around with circular manner
                diff = (ord(s[idx]) - ord(s[idx - 1])) % 26
                pattern.append(diff)
                
            return tuple(pattern) # O(k)

        # group in dictionary
        group = defaultdict(list)

        for string in strings:
            pattern = getPattern(string)
            group[pattern].append(string)
            
        return list(group.values())
"""
Pattern 
(1,1) -> xyz - yza - abc - bcd
ba (-1)%26 =  az 25 -> az - ba 
() -> a - z

pattern:
diff (asci s[i] - s[i - 1])
Forward Wrap: ab = b - a = 1
backward wrap: ba = a - b = -1 % 26 = 25
wrap - negative = negative % wrap if abs(negative) < wrap
ba (-1)%26 = 25
(-25)%26 = 1
"""
###
"""
getPattern:
pattern should be immutable(unchangable) - hashable
list are not hashable
"""
###
"""
Example:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Calculate the shift patterns:
"abc" → (1, 1)
"bcd" → (1, 1)
"acef" → (2, 2, 1)
"xyz" → (1, 1)
"az" → (25)
"ba" → (25)
"a" → ()
"z" → ()
Group strings by patterns:
(1, 1) → ["abc", "bcd", "xyz"]
(2, 2, 1) → ["acef"]
(25) → ["az", "ba"]
() → ["a", "z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
"""
##############################################################
# 35. 282. Expression Add Operators
##############################################################
class Solution:
    """
    Time: O(4^n)
    - 4 choices -> start new num or combine with previous digit + 3 operation choice
    Space: O(n)
    - recursion stack
    """
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtracking(index, value, prev, path):
            # base case
            if index == len(num):
                if value == target: result.append(path)
                return 

            for i in range(index, len(num)):
                # edge case - leading zero
                if i > index and num[index] == "0": break

                # multi digit
                current = int(num[index:i+1])

                # choices
                if index == 0:
                    # first number , no opperation
                    backtracking(i+1, current, current, path + str(current))
                else:
                    backtracking(i+1, value + current, current, path + "+" + str(current))
                    backtracking(i+1, value - current, -current, path + "-" + str(current))
                    # for undo when we want to give priority to *
                    backtracking(i+1, value - prev + (prev * current), prev * current, path + "*" + str(current))

        backtracking(0, 0, 0, "")
        return result

"""
edge: 
Leading zero
"""
"""
    Leading zero: 
    i > index ensures that we only check for leading zeros when considering multi-digit numbers.
    i: end of substring
    index: starting index of substring
    105 -> leading zero -> 05 invalid (multi digit) but 0 is valid

    undo in * - to give priority to *:
    Input: num = "232", target = 8
    Start with the first number:
    path = "2", value = 2, prev = 2.
    Add +3:
    path = "2+3", value = 5, prev = 3.
    Multiply 3 by 2:
    Expression: 2 + (3 * 2).
    Undo +3: value - prev = 5 - 3 = 2.
    Apply multiplication: 2 + (3 * 2) = 2 + 6 = 8.
    Update prev: prev = 6.
    Result:
    Expression 2 + 3 * 2 matches the target.

    Example: 2*3*4
    prev = 2*3 = 6 
    value = 6
    next step: value - pre + (pre * cur) = 6 - 6 + (6 *4) = 0 +...
"""
##############################################################
# 36. 498. Diagonal Traverse @
##############################################################
"""
Time: O(n.m)
Space: O(1)
"""
class Solution:
    def findDiagonalOrder(self, mat):
        # edge case - empty
        if not mat or not mat[0]: return []

        ROW, COL = len(mat), len(mat[0])
        result = []
        direction = 1
        row, col = 0, 0

        while len(result) != ROW*COL:
            result.append(mat[row][col])

            # out of bound
            if ((direction and (row == 0 or col == COL - 1)) 
                or (not direction and (row == ROW - 1 or col == 0))):
                if direction:
                    # up right
                    if col == COL - 1: row += 1
                    elif row == 0: col += 1
                # left down
                else:
                    if row == ROW - 1: col += 1
                    elif col == 0: row += 1
                direction = 1 - direction
                continue
            # in bound
            row, col = row + (-1 if direction else 1), col + (1 if direction else -1)
        
        return result
    def _findDiagonalOrder(self, mat):
        # edge case - empty
        if not mat or not mat[0]: return []
        
        ROW, COL = len(mat), len(mat[0])

        cur_row, cur_col = 0, 0
        up_right = True
        result = []

        while len(result) != ROW*COL:
            result.append(mat[cur_row][cur_col])

            if up_right:
                # out of bound
                if cur_col == COL - 1:
                    cur_row += 1
                    up_right = False
                elif cur_row == 0:
                    cur_col += 1
                    up_right = False

                # move
                else:
                    cur_row -= 1
                    cur_col += 1
            else:
                # out of bound
                if cur_row == ROW - 1:
                    cur_col += 1
                    up_right = True
                elif cur_col == 0:
                    cur_row += 1
                    up_right = True
                # move
                else:
                    cur_row += 1
                    cur_col -= 1

        return result
"""
mat = [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,4,7,5,3,6,8,9]
up-right row- col+
bound: row 0, col+
       col n-1, row +1
down-left row+ col-
        row n-1 col+
        col 0 row+

"""
class Solution:
    """
    Time: O(n.m)
    Space: O(n+m)
    - n + m - 1 diagnal
    """
    def findDiagonalOrder(self, mat: List[List[int]])-> List[int]:
        ROW, COL = len(mat), len(mat[0])

        # group each diagonal
        record_diagnal = defaultdict(list)
        for row in range(ROW):
            for col in range(COL):
                diagonal = row + col
                record_diagnal[diagonal].append(mat[row][col])

        # extend all values in diagonal in correct order
        result = []
        for diagonal, value in sorted(record_diagnal.items()):
            # even
            if diagonal % 2 == 0:
                result.extend(value[::-1])
            # odd
            else:
                result.extend(value)

        return result
"""
0 -> 1
1 -> 2, 4
2 -> 3, 5, 7 -> reverse
"""
##############################################################
# 37. 415. Add Strings
##############################################################
class Solution:
    """
    Time: O(max(n,m))
    Space: O(max(n,m))
    """
    def addStrings(self, num1:str, num2:str)->str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        value = 0
        result = []
        # 19, 1
        while p2 >= 0 or p1 >= 0 or carry > 0:
            # convert
            val1 = ord(num1[p1]) - ord("0") if p1 >= 0 else 0
            val2 = ord(num2[p2]) - ord("0") if p2 >= 0 else 0
            
            value = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            result.append(str(value))

            p1 -= 1
            p2 -= 1

        return "".join(result[::-1])
"""
pointer: end to start
carry: nums // 10
value: nums % 10
"""
"""
adv ord to int
- overhead - handle errors (invalid logic)
- faster for long string
"""
##############################################################
# 38. 317. Shortest Distance from All Buildings
##############################################################
"""
Time: O(B*n*m)
- B: number of building
Space: O(n*m)
"""
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # edge case 
        if not grid or not grid[0]: return -1

        ROW, COL = len(grid), len(grid[0])

        distance = [[0] * COL for _ in range(ROW)]
        reachable = [[0] * COL for _ in range(ROW)]
        def bfs(row, col):
            direction = [(0,1),(0,-1),(1,0),(-1,0)]
            queue = deque([(row, col,0)])
            visited = set((row, col))

            while queue:
                cur_row, cur_col, dist = queue.popleft()
                for row_dir, col_dir in direction:
                    new_row, new_col = cur_row + row_dir, cur_col + col_dir

                    # check bounds
                    if (not 0 <= new_row < ROW
                        or not 0 <= new_col < COL
                        or (new_row, new_col) in visited
                        or grid[new_row][new_col] != 0): 
                        continue
                    
                    visited.add((new_row, new_col))
                    distance[new_row][new_col] += dist + 1
                    reachable[new_row][new_col] += 1
                    queue.append((new_row, new_col, dist + 1))

        # traverse
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    # distance and reachable
                    bfs(row, col)

        # find the minimum distance
        min_distance = float("inf")
        building = sum(row.count(1) for row in grid)
        for row in range(ROW):
            for col in range(COL):
                if reachable[row][col] == building and grid[row][col] == 0:
                    min_distance = min(min_distance, distance[row][col])

        return min_distance if min_distance != float("inf") else -1

"""
Grid:
1 0 1
0 2 0
0 0 0

bfs for (0,0)
distance
0 1 0
1 0 0
2 3 4
reachable
0 1 0
1 0 0
1 1 1

bfs for (0,2)
distance
0 2 0
1 0 1
2 3 6
reachable
0 2 0
1 0 1
1 1 2
"""
##############################################################
# 39. 163. Missing Ranges
##############################################################
class Solution:
    """
    time: o(n)
    space: O(1 or n)
    missed n
    """
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missed = []

        pre = lower - 1

        for num in nums:
            if pre + 1 < num:
                missed.append([pre + 1, num - 1])
            pre = num

        if pre + 1 <= upper:
            missed.append([pre + 1, upper])

        return missed
    
    def _inefficientFindMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missed = []
        
        if nums and lower < nums[0]:
            missed.append([lower, nums[0] - 1])

        low, high = 0, 1
        while high < len(nums):
            if nums[low] + 1 < nums[high]:
                missed.append([nums[low] + 1, nums[high] - 1])
            low += 1 
            high += 1

        if nums and nums[-1] < upper:
            missed.append([nums[-1] + 1, upper])
        if not nums:
            missed.append([lower, upper])

        return missed
##############################################################
# 40. 398. Random Pick Index
##############################################################
"""
reservoir sampling algorithm -> pick each specific index is uniformly 1/count (equal possibility)
"""
class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        total_found, index_choice = 0, -1
        for idx, num in enumerate(self.nums):
            if num == target:
                total_found += 1
                # check == 1 gives exactly a 1-in-total_found chance to pick the current index
                if random.randint(1,total_found) == 1:
                    index_choice = idx
        return index_choice
    """
    Time: O(n)
    Space: O(n)
    pick func:
    Time&space: O(1)
    """
    def __init__(self, nums: List[int]):
        self.indeces = defaultdict(list)

        for idx, num in enumerate(nums):
            self.indeces[num].append(idx)

    def pick(self, target: int)->int:
        return random.choice(self.indeces[target])
##############################################################
# 41. 489. Robot Room Cleaner
##############################################################
##############################################################
# 42. 1216. Valid Palindrome III
##############################################################
class Solution:
    """
    Optimized: Least Recently Used Cache
    With memoization
    Time: O(n^2 * k)
    Space: O(n^2 * k + k)
    - memoization: n ^ 2 * k 
    """
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # memoization - unique state
        @lru_cache(None)
        def isPalindrome(left, right, k):
            while left < right:
                if s[left] != s[right]:
                    # base case
                    if k <= 0: return False
                    # remove a character from left or right
                    return isPalindrome(left + 1, right, k - 1) or isPalindrome(left, right - 1, k - 1)
                left += 1
                right -= 1
            return True

        return isPalindrome(0, len(s) - 1, k)
    
    def isValidPalindrome1(self, s: str, k: int) -> bool:
        left, right = 0, len(s) - 1

        @lru_cache(maxsize=100)
        def isValid(left, right, counter):
            if left >= right: return True

            if s[left] != s[right]:
                if counter >= k: return False

                return isValid(left + 1, right, counter + 1) or isValid(left, right - 1, counter + 1)
            
            return isValid(left+1, right - 1, counter)
        
        return isValid(left, right, 0)

    def isValidPalindrome2(self, s: str, k: int) -> bool:
        left, right = 0, len(s) - 1
        @lru_cache(maxsize=100)
        def isValid(left, right, k):
            if left >= right: return True

            if s[left] != s[right]:
                if k <= 0: return False

                return isValid(left + 1, right, k - 1) or isValid(left, right - 1, k - 1)
            
            return isValid(left+1, right - 1, k)
        
        return isValid(left, right, k)
"""
without memoization:
Time: O(2 ^ k)
- 2 recursive call for each mismatch
- if k is small
- k depth of recursion
Space: O(k)
- recursive call stack

"""
###
"""
lru_cache(None):
- # None means unlimited cache size
- @lru_cache(maxsize=100, typed=True)
- The "Least Recently Used" part means that when the cache reaches its maximum size (default is 128 entries), the least recently used results are discarded to make room for new ones.
"""
##############################################################
# 43. 523. Continuous Subarray Sum - *Jog
##############################################################
class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def checkSubarraySum(self, nums, k):
        seen = {0: -1}
        prefix_sum = 0

        for idx, num in enumerate(nums):
            prefix_sum += num
            modular_prefix = prefix_sum % k

            # check existance of prefix sum
            if modular_prefix in seen:
                if idx - seen[modular_prefix] > 1:
                    # there is a good subarray that is multiple of k
                    return True

            # update 
            else:
                # The first time occurrence of remainder
                seen[modular_prefix] = idx
        
        return False
"""
When prefix mod k is already in seen, it implies:
There was an earlier prefix sum with the same remainder.
The difference between the two prefix sums is a multiple of k

subarray sum = prefix j - prefix i
(prefix j - prefix i) % k = 0
(prefix j) % k = (prefix i) % k

[23,2,4,6,7], k = 6 -> 2,4 -> T
[23,25,29,35,42]
[5,1,5,5,0]
29 - 23 = 6

[23,2,6,4,7], k = 6 -> 42 = 7 * 6 -> T
[23,25,31,35,42]
[5,1,1,5,0]
35 - 23 = 12 / 6

[2,4], k = 2 -> 2 + 4 = 6 = 2 * 3

prefix % k equal and exist -> same remainder means -> The sum of the subarray between those indices cancels out the earlier contribution (from the first occurrence of the remainder) and leaves a multiple of 𝑘
length > 1 -> idx - previous idx 
"""
##############################################################
# 44. 766. Toeplitz Matrix
##############################################################
class Solution:
    """
    check with top left
    
    Time: O(n.m)
    Space: O(1)
    """
    def isToeplitzMatrix(self, matrix):
        # traverse
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                # mismatch with top left
                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False
        return True
"""
Group by category
T: O(n.m)
S: O(m+n)
"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
##############################################################
# 45. 301. Remove Invalid Parentheses
##############################################################
"""
Removes the minimum number of invalid parentheses to make the input string valid.
Returns all possible results without duplicates.
"""
class Solution:
    """
    Time: O(2^n . n)
    - 2^n state: decide keep or remove the character (can be generated (removing each parenthesis one by one))
    - n check is valid
    Space: O(2^n)
    """
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = deque([s])
        # convert list of string not string # {"x("} instead of {"x", "("}
        visited_substring = set([s])
        found_min_level = False
        result = []
        while queue:
            current_sub = queue.popleft()
            
            # check valid substring
            if self.isValid(current_sub):
                result.append(current_sub)
                found_min_level = True

            # check early found in current level and dont explore further levels
            if found_min_level:
                continue

            # level check - not found
            # Generate all possible states by removing one parenthesis at a time
            for i in range(len(current_sub)):
                # skip 
                if current_sub[i] not in ("(",")"): continue

                # after skiping current char
                next_sub = current_sub[:i] + current_sub[i+1:]

                if next_sub not in visited_substring:
                    queue.append(next_sub)
                    visited_substring.add(next_sub)
        # min removal for substrings
        return result if result else [""]

    def isValid(self, string):
        count = 0

        for char in string:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1

            if count < 0:
                return False

        return count == 0

"""
Level 0:         (a)())()
                /   |   |   \
Level 1:  a)())()  (a())()  (a)))()  (a)()()
              \      \      /    \
Level 2:  (results found; stop further exploration)


Valid Strings Found: ["(a())()", "(a)()()"]
"""
##############################################################
# 46. 173. Binary Search Tree Iterator
##############################################################
"""
Inorder tree traversal
flatten tree
"""
class BSTIterator:
    """
    Time: O(N)
    Space: O(N)
    """
    def __init__(self, root: TreeNode):
        self.inorder_list = []
        self.index = -1
        self._inorder(root)

    def _inorder(self, node: TreeNode):
        # base case 
        if not node: return None

        self._inorder(node.left)
        self.inorder_list.append(node.val)
        self._inorder(node.right)

    def next(self):
        self.index += 1
        return self.inorder_list[self.index]

    def hasNext(self):
        return self.index + 1 < len(self.inorder_list)
##############################################################
# 47. 270. Closest Binary Search Tree Value
##############################################################
class Solution:
    """
    Time: O(logn) 
    - since here one goes from root down to a leaf.
    Space: O(1)
    """
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val

        while root:
            # check closest - multiple answer -> smallest
            if (abs(target - root.val) < abs(target - closest) 
                or (abs(target - root.val) == abs(target - closest) and closest > root.val)):
                closest = root.val
            # move based on target distance
            root = root.left if root.val > target else root.right

        return closest
##############################################################
# 48. 1428. Leftmost Column with at Least a One
##############################################################
class BinaryMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def dimensions(self) -> list:
        return [len(self.matrix), len(self.matrix[0])]
"""
right-top -> sorted
"""
class Solution:
    """
    T: O(n+m)
    S: O(1)
    """
    def leftMostColumnWithOne(self, mat: 'BinaryMatrix')->int:
        # Greedy
        ROW, COL = mat.dimensions()
        # right left
        cur_row, cur_col = 0, COL - 1
        leftmost_col = -1

        while cur_row < ROW and cur_col >= 0:
            if mat.get(cur_row, cur_col) == 1: 
                leftmost_col = cur_col
                # move left
                cur_col -= 1
            else:
                # move down
                cur_row += 1
        
        return leftmost_col 
"""
Input: mat = [[0,0],[0,0]]
Output: -1
"""
"""
Inefficient: linear search in row * col
"""
##############################################################
# 49. 2060. Check if an Original String Exists Given Tw
##############################################################
##############################################################
# 50. 1891. Cutting Ribbons
##############################################################
class Solution:
    """
    Time: O(nlogn)
    Space: O(1)
    """
    def maxLength(self, ribbons: List[int], k:int)-> int:
        left, right = 1, max(ribbons)
        result = 0

        while left <= right:
            mid = left + (right - left) // 2

            if self.isFeasible(mid, ribbons,k):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result

    def isFeasible(self, max_length, ribbons, k):
        piece = 0

        for ribbon_length in ribbons:
            piece += ribbon_length // max_length

            if piece >= k:
                return True

        # not feasible
        return False
"""
return maximum length of ribbon, x, that allows you to cut at least k ribbons, each of length x. You can discard any leftover ribbon from the cuts. If it is impossible to cut k ribbons of the same length, return 0.
"""
"""
ribbons = [9,7,5], k = 3 same length -> max length

9/5 = 1 
7/5 = 1
5/5 = 1
sum = 3 piece

1. find max in range 1 - max(9)
2. feasibility check yes/no for mid length
"""
"""
Input: ribbons = [5,7,9], k = 22
Output: 0
"""