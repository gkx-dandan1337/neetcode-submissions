class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = [] 
        def dfs(i):
            if i >= len(nums):
                res.append(path.copy())
                return
            #take 
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            #skip
            dfs(i+1)
        
        dfs(0)
        return res
