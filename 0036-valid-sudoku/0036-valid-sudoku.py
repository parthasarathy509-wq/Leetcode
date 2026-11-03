from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create sets to keep track of seen numbers for rows, columns, and 3x3 blocks
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty positions
                if val == '.':
                    continue
                
                # Determine which 3x3 box index (0 to 8) we are currently in
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check for duplicates in the current row, column, or 3x3 box
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                # If it's a new number, add it to our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True
