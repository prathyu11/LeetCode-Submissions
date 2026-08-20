class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target>matrix[-1][-1] or target<matrix[0][0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = m*n - 1

        while i<=j:
            mid = i+(j-i)//2
            val = matrix[mid//n][mid%n]
            if val == target:
                return True
            elif target>val:
                i=mid+1
            else:
                j=mid-1
        return False


