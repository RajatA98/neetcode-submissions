from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Traverse through the board 
        #create 3 maps
        #map1 rows k 0 - 8 v set of nums
        #map2 columns 
        #map3 boxes k assign cordinates v set of nums
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                b_k = (r//3, c//3)
                #if '.' skip
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[b_k]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boxes[b_k].add(board[r][c])
        return True

        

        