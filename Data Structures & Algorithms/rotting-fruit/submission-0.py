class Solution:
    def orangesRotting(self, grid: List[List[int]])-> int:
        '''
        varible = row , col queue and visted , frest count and mintune 
         - have a helper function for the bfs 

        - find the rotten and store it in queue and count fresht tomates
        - while loop to check if queue is empty and see if fresh is geater than zero

        -pop and then minitue plus one and when change cell that equal - 1 to zero
        ret count if fresh count = =



        ''' 
        row , col = len(grid) , len(grid[0])

        vist = set()
        fresh_count = 0
        minute_count = 0
        q = deque()
        

        def bfs(r, c):
            nonlocal fresh_count 
            if min(r, c) < 0 or r == row or c== col or grid[r][c] != 1:
                return
 
            grid[r][c] = 2
            fresh_count -= 1
            q.append([r,c])
            vist.add((r,c))
           




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

        




        