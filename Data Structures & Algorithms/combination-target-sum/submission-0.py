class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        path = []
        res = []
        def dfs(i, target):
            if target == 0:
                res.append(path.copy())
                return 
            
            if i >= len(nums):
                return 
            #take
            if target - nums[i] >= 0:
                path.append(nums[i])
                dfs(i, target-nums[i])
                path.pop()
            #skip
            dfs(i+1, target)

        dfs(0, target)
        return res


