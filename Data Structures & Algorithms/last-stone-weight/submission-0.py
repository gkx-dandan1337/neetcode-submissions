class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxheap = [-stone for stone in stones]
        import heapq
        heapq.heapify(maxheap)
        
        while maxheap and len(maxheap) >= 2:
            x,y = heapq.heappop(maxheap),heapq.heappop(maxheap)
            x,y = -x,-y

            diff = abs(x-y)
            if diff > 0:
                heapq.heappush(maxheap, -diff)
        
        if maxheap:
            return -maxheap[0]
        else:
            return 0 