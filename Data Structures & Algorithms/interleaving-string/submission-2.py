class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        dp =  {}
        if len(s1)+ len(s2) > len(s3):
            return False
        def dfs(i,j):

            if (i,j) in dp:
                return dp[(i,j)]
            
            if i >= len(s1):
                return s2[j:] == s3[i+j:]
            
            if j >= len(s2):
                return s1[i:] == s3[i+j:]

            res = False
            
            if s3[i+j] == s1[i] == s2[j]:
                res = res or dfs(i+1,j)
                res = res or dfs(i,j+1)

            else:
                if s3[i+j] == s1[i]:
                    res = res or dfs(i+1,j)
                elif s3[i+j] == s2[j]:
                    res = res or dfs(i,j+1)
            dp[(i,j)] = res
            return res

        return dfs(0,0)

