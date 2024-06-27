import collections

class Solution:
    def numIslands(self, grid):
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
    
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
solution = Solution()
island_number = solution.numIslands(grid)
print("Number of Island in grid: ", island_number)