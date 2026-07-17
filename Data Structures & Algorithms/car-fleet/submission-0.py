class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #monotonically increasing stack 

        stack = [] 
        lol = []

        for p, s in zip(position, speed):
            lol.append((p,s))

        def fn(x):
            return x[0]

        sorted_arr = sorted(lol, key=fn, reverse=True)
        #now this is sorted by the last position

        for p,s in sorted_arr:
            time_taken = (target - p ) / s 
        
            if stack and time_taken > stack[-1] or not stack:
                stack.append(time_taken)

        return len(stack)

            
            