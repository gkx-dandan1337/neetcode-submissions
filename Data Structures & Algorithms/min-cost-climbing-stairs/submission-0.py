class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = {} 
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(cost):
                return 0

            total = float("inf")

            if i + 1 <= len(cost):
                total = min(dfs(i+1) + cost[i], total)
            if i + 2 <= len(cost):
                total = min(dfs(i+2) + cost[i], total)
            
            dp[i] = total 
            return total 
        return min(dfs(0), dfs(1))