class Solution:
    def rob(self, nums: List[int]) -> int:
        

        dp = {} 

        def dfs(i):
            if i >= len(nums):
                return 0 
            if i in dp:
                return dp[i]
            maximum = -float("inf")
            #take 
            maximum = max(dfs(i+2) + nums[i], dfs(i+1))

            dp[i] = maximum
            return maximum
        return dfs(0)