class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l = 0 
        r = (rows) * (cols) - 1 

        while l <= r:
            mid = (l+r) // 2
            
            x,y = mid // cols, mid % cols
            
            if matrix[x][y] < target:
                l = mid + 1 
            elif matrix[x][y] > target:
                r = mid - 1 
            else:
                return True
        return False 
    

            

            


