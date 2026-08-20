class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target>matrix[-1][-1] or target<matrix[0][0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1

        while i<m and j>=0:
            
            if target > matrix[i][j]:
                i +=1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True
        return False
        

            

        

