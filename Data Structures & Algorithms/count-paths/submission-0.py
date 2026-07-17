class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {} 
        def dfs(r,c):
            if r == m - 1 and c == n -1 :
                return 1
            if r >= m or c >= n:
                return 0 
            
            if (r,c) in dp:
                return dp[(r,c)]
            ways = 0 
            ways += dfs(r+1,c)
            ways += dfs(r,c+1)
            dp[(r,c)] = ways
            return ways 
        return dfs(0,0)
            