class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = -float("inf")
        
        nodup = set(nums)

        for num in nums:
            if num - 1 not in nodup:
                count = 1 
                temp = num
                while temp + 1 in nodup:
                    temp += 1
                    count += 1
                longest = max(longest, count)
        return longest if longest != float("-inf") else 0
            


