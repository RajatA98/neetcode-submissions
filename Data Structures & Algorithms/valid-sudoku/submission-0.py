from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #3 things to check
        #no duplicates in rows 
        #no duplicates in columns
        #no duplicates in 3x3 box
        v_r = defaultdict(set)
        v_c = defaultdict(set)
        v_b = defaultdict(set)

        #create keys with empty sets 
        v_r = {i: set() for i in range(9)}
        v_c = {i: set() for i in range(9)}
        v_b = {(i, j): set() for i in range(3) for j in range(3)}

        #traverse through the board

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                b_k = (r // 3, c // 3)

                if board[r][c] in v_r[r] or board[r][c] in v_c[c] or board[r][c] in v_b[b_k]:
                    return False
                v_r[r].add(board[r][c])
                v_c[c].add(board[r][c])
                v_b[b_k].add(board[r][c])
        return True


