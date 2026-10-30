class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visted = set()
        island = 0
        res = 0

        row , col = len(grid), len(grid[0])


        def dfs(r , c):
            if r < 0 or r > row -1  or c < 0 or c > col -1 or (r ,c) in visted or grid[r][c] == 0:
                return 0
            visted.add((r , c ))

            area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1)+  dfs(r, c - 1)
            return area


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r ,c ) not in visted:
                    island = dfs(r, c)

                res = max(res , island)
        return res
            
        