class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count= 0 
        visted= set()
        row, cols = len(grid) ,len(grid[0])
        

        def dfs(r, c):
            if r < 0 or r > row -1 or c < 0 or c > cols - 1 or (r, c) in visted or grid[r][c] == "0":
                return
            visted.add((r , c))
                            
            dfs(r + 1 , c)
            dfs(r - 1 , c)
            dfs(r , c + 1)
            dfs(r , c - 1)



        for r in range(row):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visted:
                    count += 1
                    dfs( r, c)

        return count