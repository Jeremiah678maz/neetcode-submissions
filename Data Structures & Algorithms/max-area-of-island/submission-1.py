class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row , col = len(grid), len(grid[0])
        visted = set()
        island = 0
        maxArea = 0


        def dfs(r,c):
            if r < 0 or r > row -1  or c < 0 or c > col -1  or grid[r][c] == 0 or (r ,c ) in visted:
                return 0
            visted.add((r, c))
            maxIsland = 1 + dfs(r + 1,c) + dfs(r -1,c) + dfs(r,c -1) + dfs(r, c + 1)

            return maxIsland

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visted:

                    
                    island = dfs(r,c )
                maxArea = max(maxArea, island)




        return maxArea

                    
        