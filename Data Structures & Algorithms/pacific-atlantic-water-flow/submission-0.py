class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac , atl = set(), set()

        rows, cols = len(heights), len(heights[0])

        res = [] 

        def dfs(r,c, sea):
            if (r,c) in sea:
                return 
            
            sea.add((r,c))

            for dr, dc in [(0,1),(1,0), (-1,0),(0,-1)]:
                nr, nc = r + dr , c + dc 
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,sea)

        for r in range(rows):
            dfs(r,0,pac)
        
        for c in range(cols):
            dfs(0,c,pac)

        
        for r in range(rows):
            dfs(r,cols-1, atl)
        
        for c in range(cols):
            dfs(rows-1,c,atl)

        for r,c in pac:
            if (r,c) in atl:
                res.append((r,c))
        return res
        


        