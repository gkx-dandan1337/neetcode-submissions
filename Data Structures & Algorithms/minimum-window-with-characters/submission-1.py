class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0 
        shortest = float("inf")
        freq = {} 

        if len(t) > len(s):
            return ""

        for char in t:
            if char not in freq:
                freq[char] = 0 
            freq[char] += 1

        have = 0 
        required = len(freq)
        pointers = float("inf"), float("inf")

        for r, char in enumerate(s):
            if char in freq:
                freq[char] -= 1
                if freq[char] == 0:
                    have += 1
            
            while have == required:
                length = r-l+1
                if length < shortest:
                    shortest = length
                    pointers = l,r

                el = s[l]
                if el in freq:
                    if freq[el] == 0:
                        have -= 1
                    freq[el] += 1
                
                l+=1
           
        if pointers[0] == float("inf") or pointers[1] == float("inf"):
            return ""
        else:
            return s[pointers[0] : pointers[1]+1]
            

            