class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row , col = len(grid) , len(grid[0])
        island = 0
        visted = set()

        def dfs(r , c):
            if r < 0 or r > row -1 or c < 0 or c > col -1 or (r,c ) in visted or grid[r][c] == "0":
                return
            visted.add((r,c)) 
            dfs(r + 1 , c)
            dfs(r - 1 , c)
            dfs(r  , c+ 1)
            dfs(r, c -1 )

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visted:
                    island += 1

                    dfs(r,c)
        return island




        