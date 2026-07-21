class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r,c):

            if (r,c) in dp:
                return dp[(r,c)]
            
            best = 1 
            for dr, dc in [(0,1), (1,0), (-1,0),(0,-1)]:
                nr, nc = r +dr, c +dc 
                if 0<= nr<rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr,nc))

            dp[(r,c)] = best
            return best 
        res = -float("inf")
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r,c))
        return res
