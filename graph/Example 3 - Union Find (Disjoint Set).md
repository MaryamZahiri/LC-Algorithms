# Graph Algorithm - Union Find (Disjoint Set)
The primary use of disjoint sets is to address the ```connectivity``` between the components of a network. 
For instance, we can use a disjoint set to determine if two people share a common ancestor.

## 
## Quick Find

<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/a7dfc4f2-9399-4f5b-8927-343a874393e7" width=250><br />

<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/a0858062-f7b0-406e-86d2-9a4e82255f70" width=250><br />

```python 
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        # if they are connected, no need for union function
        rootX = self.find(x)
        rootY = self.find(y)
        # if their root are not the same, union them
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

```python
# 1-2-5-6-7 3-8-9 4
uf = UnionFind(10)

uf.union(1,2)
uf.union(2,5)
uf.union(5,6)
uf.union(6,7)

uf.union(3,8)
uf.union(8,9)

print(uf.connected(1,5)) #True
print(uf.connected(4,9)) #False
```

Time Complexity: O(N) because we need to traverse through the entire array

Space Complexity: O(N) space to store the array of size N.

##
## Quick Union

##
## Optimization
- Union by Rank
- Path Compression Optimization
- Optimized “disjoint set” with Path Compression and Union by Rank

## Terms
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/4085b078-10d1-4f25-b493-a004fae29e21" width=250><br />

- Parent node: the direct parent node of a vertex. For example, in Figure , the parent node of vertex 3 is 1, the parent node of vertex 2 is 0, and the parent node of vertex 9 is 9.
- Root node: a node without a parent node; it can be viewed as the parent node of itself. For example, in Figure, the root node of vertices 3 and 2 is 0.

- Find Function
- Union Function

# LeetCode Problem 200: [Questions](https://leetcode.com/problems/)
## Problem Description
## Solution Approaches

### --- Algorithm
Algorithm Pattern:

1. Initialization:
    - Determine 
## Example Description

## Python Code
```python
```
## Complexity Analysis
- Time complexity : 

- Space complexity :