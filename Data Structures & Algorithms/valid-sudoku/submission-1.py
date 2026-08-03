from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                boxid = (r//3,c//3)
        
                if (val in rows[r] or val in cols[c] or val in boxes[boxid]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[boxid].add(val)

        return True