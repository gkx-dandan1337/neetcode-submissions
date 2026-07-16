class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)

        def can_finish(rate):
            total = 0 
            for pile in piles:
                hours = pile // rate
                total += hours
                if pile % rate >0:
                    total += 1
            return total <= h

        while l < r:

            mid = (l+r) // 2
            if can_finish(mid):
                r = mid 
            else:
                l = mid + 1 
        
        return r

