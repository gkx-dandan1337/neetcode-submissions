class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {} 
        def dfs(i, target):
            if (i,target) in dp:
                return dp[(i,target)]
            if i == len(nums) and target ==0 :
                return 1
            
            if i >= len(nums):
                return 0 
            

            ways = 0 
            ways += dfs(i+1, target - nums[i])
            ways += dfs(i+1, target + nums[i])
            dp[(i,target)] = ways 

            return ways 
        return dfs(0,target)
        