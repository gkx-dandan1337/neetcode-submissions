class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        fruits = 0 
        visited = set()

        from collections import deque
        queue = deque() 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fruits += 1 
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
        time = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                
                for dr, dc in [(0,1),(1,0), (-1,0),(0,-1)]:
                    nr, nc = r + dr , c + dc 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visited: 
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        fruits -= 1 
            if queue:  
                time += 1
        return time if fruits == 0 else -1


        
