class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        row = len(grid)
        col = len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for x,y in dirs:
                dfs(r + x, c + y)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res