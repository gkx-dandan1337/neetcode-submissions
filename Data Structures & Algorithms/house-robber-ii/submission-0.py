class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            dp = {}

            def dfs(i):
                if i in dp:
                    return dp[i]
                if i >= len(arr):
                    return 0
                
                dp[i] = max(dfs(i+2) + arr[i], dfs(i+1))
                return dp[i]

            return dfs(0)

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))