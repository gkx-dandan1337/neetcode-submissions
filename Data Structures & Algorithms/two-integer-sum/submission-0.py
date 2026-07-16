class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashmap  = {} 
        #we assume that all the numbers are unique
        for r, num in enumerate(nums):
            hashmap[num] = r 

        for r, num in enumerate(nums):
            comp = target - num 
            if comp in hashmap and hashmap[comp] != r :
                return [r,hashmap[comp]]
        