class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {} 

        def dfs(target):
            if target in dp:
                return dp[target]
            if target == 0:
                return 0 
            res = float("inf")
            for coin in coins:
                if target - coin >= 0:
                    res = min(res, 1 + dfs(target-coin))
            
            dp[target] = res
            return res 
        
        ans = dfs(amount)
        return ans if ans != float("inf") else -1             
            
            