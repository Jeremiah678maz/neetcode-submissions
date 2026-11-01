class Solution:
    def orangesRotting(self, grid: List[List[int]])-> int:
        
        row , col = len(grid) , len(grid[0])

        vist = set()
        fresh_count = 0
        minute_count = 0
        q = deque()
        

        def bfs(r, c):
            nonlocal fresh_count  ## this is bfs multisource bfs go layer by layer
            if min(r, c) < 0 or r == row or c== col or grid[r][c] != 1:
                return #checks base case
 
            grid[r][c] = 2  #changes current grid to 2 and reduce count and add new cell
            fresh_count -= 1
            q.append([r,c])
            
           
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r,c])
                    vist.add((r,c))
                if grid[r][c] == 1:
                    fresh_count += 1

        while q and fresh_count > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            minute_count += 1

        return minute_count if fresh_count == 0 else -1

        




        