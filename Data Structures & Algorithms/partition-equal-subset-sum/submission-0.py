class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        dp = {} 
        total = sum(nums)
        if total % 2:
            return False 
        half = total // 2 

        def dfs(i, target):
            if (i,target) in dp:
                return dp[(i,target)]

            if target == half:
                return True 

            if i >= len(nums):
                return False 
            res = False 
            if target + nums[i] <= half:
                res = res or dfs(i+1, target + nums[i])
            
            res = res or dfs(i+1, target)
            dp[(i,target)] = res 
            return res 
        return dfs(0,0)
            
            
            