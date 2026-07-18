class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {} 
        
        def dfs(i, holding):

            if (i, holding) in dp:
                return dp[(i,holding)]

            if i >= len(prices):
                return 0 

            res = 0 

            if holding: 
                sell = dfs(i+2, not holding) + prices[i]
                skip = dfs(i+1, holding)
                res = max(res, sell, skip)
            else:
                buy = dfs(i+1, not holding) - prices[i]
                skip = dfs(i+1, holding)
                res = max(res, buy, skip)

            dp[(i, holding)] = res 
            return res
            

        return dfs(0, False)


            
            