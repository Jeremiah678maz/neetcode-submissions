class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row , col = len(matrix) , len(matrix[0])
        
        R , C = row - 1 , 0

        while R >= 0 and C < col:
            if matrix[R][C] == target:
                return True
            elif matrix[R][C] > target:
                R -= 1
            elif matrix[R][C] < target:
                C += 1 
        return False