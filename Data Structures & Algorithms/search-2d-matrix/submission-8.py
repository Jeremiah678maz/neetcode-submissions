class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M , N = len(matrix) , len(matrix[0])

        R ,C = M -1 , 0

        while R >= 0 and C <  N:
            if matrix[R][C] > target:
                R -= 1
            elif matrix[R][C] < target:
                C += 1
            elif matrix[R][C] == target:
                return True
        return False
