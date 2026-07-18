class Solution:
    def longestPalindrome(self, s: str) -> str:
        maximum = 0
        res = ""
        def check(i, j) -> bool:
            nonlocal maximum
            nonlocal res
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > maximum:
                    maximum = j-i+1
                    res = s[i:j+1]
                j+=1
                i-=1

        for i in range(len(s)-1):
            check(i, i+1)
        
        for i in range(len(s)):
            check(i, i)
        
        return res




