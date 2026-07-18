class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        dp = {} 
        wordset = set(wordDict)

        def dfs(i): #returns true or false 

            if i in dp:
                return dp[i]
            
            if i >= len(s):
                return True 

            res = False 
            for word in wordset:
                n = len(word)
                if s[i:i+n] == word:
                    res = res or dfs(i+n)
            
            dp[i] = res
            return res 
        return dfs(0)
            
            

