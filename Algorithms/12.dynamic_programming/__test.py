def maxProfitUniquePath(grid):
    row = len(grid)
    col = len(grid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = grid[0][0]
    print(row, col)
    print(dp)
    for i in range(row):
        for j in range(col):
            print(i,j)
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            elif j > 0 and i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
    return dp[row-1][col-1]

grid = [[1,2,3,2],[4,3,2,3],[4,2,5,4]]
test = maxProfitUniquePath(grid)
print(test)