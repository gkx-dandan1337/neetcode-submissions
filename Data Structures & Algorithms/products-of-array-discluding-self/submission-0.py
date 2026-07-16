class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        #we want to find the product of everythign that is except itself

        #brute force approach is to loop through everything, becomes n^2 

        pre = [1]*len(nums)
        suff = [1]*len(nums)

        for i in range(1,len(pre)):
            pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(len(suff)-2,-1,-1):
            suff[i] = suff[i+1] * nums[i+1]
        
        res = [1] * len(nums)
        for i in range(len(res)):
            res[i] = pre[i] * suff[i]
        return res