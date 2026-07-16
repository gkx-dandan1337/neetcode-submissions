class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        from collections import defaultdict

        square, row, col = defaultdict(set),defaultdict(set),defaultdict(set)
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                el = board[r][c]
                if el == ".":
                    continue
                if el in row[r] or el in col[c] or el in square[(r//3,c//3)]:
                    return False 
                row[r].add(el)
                col[c].add(el)
                square[(r//3,c//3)].add(el)
        return True