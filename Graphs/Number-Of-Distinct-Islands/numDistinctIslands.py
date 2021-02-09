# Time Complexity = O(nm) | Space Complexity = O(nm), where n is the number of rows, m is the number of columns

class Solution:
    def numDistinctIslands(self, grid):
        if grid == None or len(grid) == 0: return 0
        distinctIslands = set()
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    path = self.dfs(grid, row, col, rows, cols, "X")
                    distinctIslands.add(path)
        return len(distinctIslands)
    
    def dfs(self, grid, row, col, rows, cols, direction):
        
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
            return "O"
        
        grid[row][col] = 0
        left = self.dfs(grid, row, col - 1, rows, cols, "L")
        right = self.dfs(grid, row, col + 1, rows, cols, "R")
        up = self.dfs(grid, row - 1, col, rows, cols, "U")
        down = self.dfs(grid, row + 1, col, rows, cols, "D")
        
        return direction + left + right + up + down