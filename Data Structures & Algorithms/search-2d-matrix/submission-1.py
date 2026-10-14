class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N , M = len(matrix) , len(matrix[0])
        row, col = N - 1, 0

        while row >= 0 and col < M:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False
