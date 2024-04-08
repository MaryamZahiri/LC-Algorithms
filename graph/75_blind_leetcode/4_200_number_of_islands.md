# LeetCode Problem 200: [Number of Islands](https://leetcode.com/problems/number-of-islands/)
## Problem Description
Given a 2D grid grid of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. Assume all four edges of the grid are all surrounded by water.
## Solution Approaches
### BFS Algorithm
- Data Structure: 
    - visited: set
    - row, col: variables to traverse the grid and track 
    - island counter: output variable
    - queue: memory to track the cell of grid
- Steps:
    - Initialize variables and data structure 
    - Traverse the grid by 2 for loop 
    - Whenever we encounter a land cell '1' that hasn't been visited, we call bfs function to check the visited status and land cell for 4 neighbors of the cell
    - Then increment the count of islands
        - In BFS function, initialize queue and visited. 
        - While our queue is not empty, update current row and current column by popping the first cell in queue 
        - Define direction (2d array) for right, left, up, down neighbors of each cell 
        - While looping to check 4 direction of each cell, we check if the current cell is in bound, not visited and land cell is "1"
        - Update the row and colomn direction based on 4 directions horizontally and virtically 
        - Then, add it to visited set and append it to queue memory
    - return number of counted islands
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