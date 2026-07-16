class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False 

        from collections import Counter
        
        counts = Counter(s1)
        l = 0 
        have = 0 
        required = len(counts)

        for r, char in enumerate(s2):
            if char in counts:
                counts[char] -= 1
                if counts[char] == 0:
                    have += 1
            
            while r-l+1 > len(s1):
                el = s2[l]
                
                if el in counts:
                    if counts[el] == 0:
                        have -= 1
                    counts[el] += 1
                l+=1
            
            if have == required:
                return True 

        return False 
                    


