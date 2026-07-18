class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        from collections import deque 
        queue = deque()
        INF = 2147483647 
        visited = set() 

        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        distance = 1
        
        #queue now has been populated with the coords 
        while queue: 
            for _ in range(len(queue)):
                r,c = queue.popleft() 
                for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                    nr,nc = dr + r , dc + c 
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == INF: 
                        visited.add((nr,nc))
                        grid[nr][nc] = distance 
                        queue.append((nr,nc))               

            distance += 1 

        
            

