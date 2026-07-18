class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = {} 
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in dp:
                return dp[i]
            
            best = 1 
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))
            
            dp[i] = best
            return best 
        best = 1 
        for i in range(len(nums)):
            best = max(best, dfs(i))
        return best 
        
            
