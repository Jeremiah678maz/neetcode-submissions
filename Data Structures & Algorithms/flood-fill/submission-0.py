class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''''
          0   1  2
      0  [ 1  1  1 ]    sr , sc ( 1, 1) color = 2
      1  [ 1  1  0 ]
      2  [ 1  0  1 ]


      
        '''''

        row, col = len(image), len(image[0])

        original = image[sr][sc]

        if original == color:
            return image

        def fill(r, c):
            if r < 0 or r >= row or c >= col or c < 0:
                return 
            if image[r][c] != original:
                return

            image[r][c] = color
            fill(r + 1, c) 
            fill(r - 1, c)
            fill(r, c + 1)
            fill(r, c - 1)

        fill(sr, sc)
        return image