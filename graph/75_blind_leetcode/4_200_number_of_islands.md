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
    - Perform BFS by dequeuing cells and enqueuing their unvisited neighbors under conditions.
3. Main Loop:
    - Iterate over each cell in the grid.
    - If a cell is land ("1") and has not been visited, call the bfs function to explore all cells connected to the current cell by visiting each neighboring cell (up, down, left, right) that is part of the island.
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
    - Iterating Over the Grid: The algorithm starts by iterating over each cell in the grid. This iteration is done in a ```nested loop```, where the outer loop iterates over the rows and the inner loop iterates over the columns. Since there are M rows and N columns, the total number of iterations is M×N.
    - BFS for Each Island: For each cell that is identified as part of an island (i.e., a cell with a value of "1" that has not been visited yet), the BFS algorithm is called. The BFS algorithm explores all cells connected to the current cell by visiting each neighboring cell (up, down, left, right) that is part of the island. This exploration is done by adding each neighboring cell to a queue and then processing each cell in the queue, which involves checking its neighbors.
    -Processing Each Cell: Each cell in the grid is processed at most once. When a cell is visited, it is ```added to the visited set, ensuring that it will not be processed again```. This ensures that the algorithm does not perform unnecessary work by revisiting cells.
    - Queue Operations: The BFS algorithm uses **a queue to keep track of cells to be visited**. In the worst-case scenario, where the grid is filled with lands (i.e., all cells are part of an island), the queue can grow to include all cells in the grid. However, this does not change the overall time complexity because the ```queue operations (adding and removing cells) are constant time operations```, and the ```total number of cells added to the queue is still proportional to the size of the grid (M×N)```.
> In summary, the time complexity is O(M×N) because the ```algorithm iterates over each cell in the grid once``` and performs ```a constant amount of work for each cell```. The **BFS algorithm's time complexity is not a factor** in the overall time complexity because it is **bounded** by the number of cells in the grid, which is M×N.

- Space complexity : O(MxN) because in worst case where the grid is filled with lands, the size of queue and visited set can store all cells of the grid and grow up to O(MxN).