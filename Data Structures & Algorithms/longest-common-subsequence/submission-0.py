class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = {} 
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i >= len(text1) or j >= len(text2):
                return 0 

            longest = 0
            if text1[i] == text2[j]:
                longest = max(1 + dfs(i+1,j+1), longest)
            else:
                longest = max(dfs(i,j+1),dfs(i+1,j))
            
            dp[(i,j)] = longest
            return longest
        return dfs(0,0)
