class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur = 0 
        res = max(nums) 
        for num in nums:
            cur += num 
            if cur < 0 :
                cur = 0 
                continue
            res = max(res, cur)
        return res
