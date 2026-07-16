class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {} 
        longest = 1
        l = 0 
        for r, char in enumerate(s):
            
            if char not in freq:
                freq[char] = 0 
            freq[char] += 1

            while (r-l+1) - max(freq.values()) > k:
                el = s[l]
                freq[el] -= 1
                l+=1
            longest = max(r-l+1, longest)
        return longest
