class Solution:
    def pacificAtlantic(self, heights):
        # Check if input is empty
        if not heights or not heights[0]: 
            return []
        
        # Initialize variables, including hash sets used to keep track of visited cells
        num_row, num_col = len(heights), len(heights[0])
        pacific_visit, atlantic_visit = set(), set()
        
        def dfs(row, col, visit, pre_height):
            # Check if the new cell is within bounds
            if row < 0 or row == num_row or col < 0 or col == num_col:
                return
            # Check that the new cell hasn't already been visited
            if (row, col) in visit:
                return
            # Check that the new cell has a higher or equal heights,
            # So that water can flow from the cell to the pre cell
            if heights[row][col] < pre_height:
                return
            
            # This cell is reachable, so mark it
            visit.add((row, col))

            # If we've gotten this far, that means the new cell is reachable
            # neighbors: dfs for 4 neighbor direction 
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        # Loop through each cell adjacent to the oceans and start a DFS
        for r in range(num_row):
            dfs(r, 0, pacific_visit, heights[r][0])
            dfs(r, num_col - 1, atlantic_visit, heights[r][num_col - 1])
        for c in range(num_col):
            dfs(0, c, pacific_visit, heights[0][c])
            dfs(num_row - 1, c, atlantic_visit, heights[num_row - 1][c])

        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_visit.intersection(atlantic_visit))
    
heights = [[1,1],[1,1],[1,1]]
solution = Solution()
common = solution.pacificAtlantic(heights)
print(common)