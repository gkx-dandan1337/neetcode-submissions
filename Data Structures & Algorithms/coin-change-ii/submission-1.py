class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp =  {}

        def dfs(i, target):
            if (i,target) in dp:
                return dp[(i,target)]

            if i >= len(coins):
                return 0

            if target == amount:
                return 1

            res = 0 
            for j in range(i, len(coins)):
                if coins[j]+ target <= amount:
                    res += dfs(j, target + coins[j])
            dp[(i,target)] = res
            return res

        return dfs(0,0)

            