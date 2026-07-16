class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq 
        minheap = []
        freq = collections.Counter(nums)
        for key, value in freq.items():
            heapq.heappush(minheap,(value, key))
        
        while len(minheap) > k:
            heapq.heappop(minheap)
        
        res = []
        for value, key in minheap:
            res.append(key)

        return res
            