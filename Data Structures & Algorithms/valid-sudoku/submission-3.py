# (don't)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        u = ord('1') # lulz

        for r in range(9):
            for c in range(9):
                v = ord(board[r][c]) - u
                if v < 0: # ord('.') is < 0 - u
                    continue;
        
                box_id = (r // 3) * 3 + (c // 3)

                if rows[r][v] or cols[c][v] or boxes[box_id][v]:
                    return False

                rows[r][v] = cols[c][v] = boxes[box_id][v] = True
    
        return True
