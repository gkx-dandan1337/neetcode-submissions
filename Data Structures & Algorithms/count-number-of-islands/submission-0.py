class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #the number of islands 
        visited = set() #stores (r,c)
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if (r,c) in visited:
                return 
            visited.add((r,c))
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = dr + r , dc + c 
                if 0<=nr<rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    dfs(nr,nc)                   
        
        islands = 0 
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands
