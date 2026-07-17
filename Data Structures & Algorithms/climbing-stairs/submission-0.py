class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {} 
        def dfs(i):
            if i >= n:
                return 1
            if i in dp:
                return dp[i]
            res = 0 
            if i + 1 <= n:
                res += dfs(i+1)
            if i + 2 <= n:
                res += dfs(i+2)
            
            dp[i] = res 
            return res 
        return dfs(0)

