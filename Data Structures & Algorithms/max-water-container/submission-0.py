class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = -float("inf")
        l,r = 0 , len(heights) - 1 

        while l < r:
            water = max(min(heights[l], heights[r]) * (r-l), water)
            
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return water
        