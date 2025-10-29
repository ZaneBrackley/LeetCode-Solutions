from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue
                box_key = (r // 3, c // 3)

                if ch in rows[r] or ch in cols[c] or ch in boxes[box_key]:
                    return False
                
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[box_key].add(ch)
        return True