class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 
        freq = {} 
        longest = 1
        if s =="":
            return 0
        for r, char in enumerate(s):
            
            if char not in freq:
                freq[char] = 0 
            freq[char] += 1
            
            while freq[char] > 1:
                el = s[l]
                freq[el] -= 1
                l+=1
            
            longest = max(longest, (r-l+1))
        return longest

