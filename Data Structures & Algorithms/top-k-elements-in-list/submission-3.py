class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort 
        from collections import Counter
        freq = Counter(nums)

        track = [[] for i in range(max(freq.values())+1)] #the max frequency that it has as the index.

        for num, val in freq.items():
            track[val].append(num)
        
        res = [] 
        for i in range(len(track)-1,-1,-1):
            for num in track[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
    