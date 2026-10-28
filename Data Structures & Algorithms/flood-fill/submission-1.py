class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orig = image[sr][sc]

       

        if orig == color:
            return image

        ROW , COL = len(image), len(image[0])
        image[sr][sc] = color
        q = deque([(sr, sc)])
        direction = [(1, 0), (-1 ,0), (0 , 1), (0 , -1)]


        while q:
            r , c = q.popleft()
            for dr , dc in direction:
                nr , nc = r + dr , c + dc
                if 0 <= nr < ROW and 0 <= nc < COL and image[nr][nc] == orig:
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image
