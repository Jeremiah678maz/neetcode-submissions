class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M , N = len(matrix) , len(matrix[0])
        
        row , col= M - 1 ,  0
        

        while row >= 0 and col < N:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row  -= 1
            elif matrix[row][col] < target:
                col += 1
        return False