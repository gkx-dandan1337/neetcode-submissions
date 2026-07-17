class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        from collections import deque

        queue = deque() #stores (frequency, alphabet, time)
        available = []  #stores (-frequency, alphabet), basically a maxheap
        freq = collections.Counter(tasks)
        for alphabet, value in freq.items():
            queue.append((value, alphabet, 0))
    
        time = 0  
        while queue or available: 
            #add the stuff from the deque into the available
            while queue and queue[0][2] <= time:
                freq, alpha, time = queue.popleft()
                heapq.heappush(available, (-freq, alpha))
            
            #pop from the available
            if available:
                freq, alpha = heapq.heappop(available)
                freq = -freq 
                freq -= 1 
                if freq > 0 :
                    nxt_time = time + n + 1 
                    queue.append((freq, alphabet, nxt_time))
                time += 1
            else:
                if queue:
                    time = queue[0][2]
        return time
        
        
                    