class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bool=False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if target==matrix[i][j]:
                    bool=True
                   
        if bool==True:
            return True
        else:
            return False
        