class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1 
        
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l+=1
                continue
            elif total > target:
                r-=1
                continue
            else:
                return [l+1,r+1]
        