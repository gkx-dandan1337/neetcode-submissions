class Solution:
    def numDecodings(self, s: str) -> int:
        
    
        dp = {}
        
        def dfs(i):
            if i >= len(s):
                return 1 
            
            if i in dp:
                return dp[i]
            
            res = 0 
            #take one 
            if s[i] != "0":
                res += dfs(i+1)
            #take two 
            if s[i] != "0" and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            
            dp[i] = res
            return res 
        return dfs(0)