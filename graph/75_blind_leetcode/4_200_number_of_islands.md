# LeetCode Problem 200: Number of Islands
## Problem Description
Given a 2D grid grid of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. Assume all four edges of the grid are all surrounded by water.
## Solution Approaches
### BFS Algorithm
- Data Structure: 
    - visited: set
    - row, col: variable for grid
    - island counter: output variable
    - queue: memory to track cell of grid
- Steps:
    - Initialize variables and data structure 
    - Traverse the grid
    - Whenever we encounter a land cell '1' that hasn't been visited, we call bfs function and increment the count of islands
    - In BFS function, we check if the current cell is in bound, not visited and land cell is "1"
    - Then, add it to visited set and append it to queue memory
## Example Description
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