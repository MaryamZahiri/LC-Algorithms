# LeetCode Problem 200: [Number of Islands](https://leetcode.com/problems/number-of-islands/)
## Problem Description
Given a 2D grid grid of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. Assume all four edges of the grid are all surrounded by water.
## Solution Approaches
### BFS Algorithm
Algorithm Pattern:
    1. Initialization:
    - Determine the dimensions of the grid (```rows and cols```).
    - Initialize a ```visited set``` to keep track of visited cells.
    - Initialize a ```counter island_num``` to count the number of islands.
    2. BFS Function:
    - Define a nested function bfs that takes a starting cell (row, col) as input.
    - Initialize a ```queue``` with the starting cell.
    - Mark the starting cell as visited.
    - Perform BFS by dequeuing cells and enqueuing their unvisited neighbors under some conditions.
    3. Main Loop:
    - Iterate over each cell in the grid.
    - If a cell is land ("1") and has not been visited, call the bfs function to explore the island starting from this cell and ```neighbors in 4 direction```.
    - Increment the island_num counter after each island is found.
    4. Return Result:
    - Return the total number of islands found.

## Example Description
BFS algorithm, traverse in each level

<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/e4fe4d8a-8747-47fb-ade3-cbdc9ca1163b" width="250"><br />

## Python Code
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_num = 0

        def bfs(row, col):
            queue = collections.deque()
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                current_row, current_col = queue.popleft()
                neighbor_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for row_dir, col_dir in neighbor_directions:
                    next_row, next_col = current_row + row_dir, current_col + col_dir
                    
                    # check if it is in boundry, skip the cell
                    if next_row not in range(rows) or next_col not in range(cols):
                        continue
                    # Check if it is visited, skip the cell
                    if (next_row, next_col) in visited:
                        continue
                    # Check if it is water
                    if grid[next_row][next_col] != "1":
                        continue

                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    island_num += 1

        return island_num
```
## Complexity Analysis
- Time complexity : O(M×N) where M is the number of rows and N is the number of columns.

- Space complexity : O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N).