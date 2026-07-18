class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0 


        def check(i,j):
            nonlocal substrings
            while i >= 0 and j < len(s) and s[i] == s[j]:
                substrings += 1
                i-=1
                j+=1
            
        for i in range(len(s)-1):
            check(i, i+1)
        for i in range(len(s)):
            check(i,i)
        
        return substrings