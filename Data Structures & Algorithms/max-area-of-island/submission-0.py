class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum = 0 

        rows, cols = len(grid), len(grid[0])

        visited = set() 

        def dfs(r,c): #this function traverses and returns the maximum area 
            
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            area = 1 
            for dr, dc in [(0,1),(1,0), (-1,0), (0,-1)]:
                nr,nc = dr +r , dc+c 
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    area  += dfs(nr,nc)
                
            return area 

        area = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(dfs(r,c),area)
        return area
        
            



