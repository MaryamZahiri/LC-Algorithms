from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        ROW, COL = len(board), len(board[0])

        for row in range(ROW):
            for col in range(COL):
                board_value = board[row][col]

                if board_value == '.': continue

                row_value = f"{row}-{board_value}"
                col_value = f"{col}-{board_value}"
                box_value = f"{(row // 3 * 3 + col // 3)}-{board_value}"    

                if (row_value in seen or
                    col_value in seen or
                    box_value in seen): return False

                seen.add(row_value)
                seen.add(col_value)
                seen.add(box_value)

        return True
    '''
    O(n^2) -> O(81) , O(81) -> O(1)
    '''
    '''
    {
    "5 in row 0":1,
    "5 in col 0":1,
    "5 in box 0":1,
    ...
    }
    '''
    def isValidSudoku3List(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                box_index = (r // 3) * 3 + (c // 3)

                if (num in rows[r] or 
                    num in cols[c] or 
                    num in boxes[box_index]):
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True