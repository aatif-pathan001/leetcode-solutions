"""
Link: https://leetcode.com/problems/valid-sudoku/description/

Problem Statement: Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
                    Each row must contain the digits 1-9 without repetition.
                    Each column must contain the digits 1-9 without repetition.
                    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Hash maps for O(1) lookup, space-time tradeoffs

Use a set() O(1) lookup instead of a nested loop. Create a set() for each row, column, and box to store seen values. 
"""


def isValidSudoku(self, board: List[List[str]]) -> bool:
  row = [set() for _ in range(9)]
  col = [set() for _ in range(9)]
  boxes = [set() for _ in range(9)]
  for r in range(9):
    for c in range(9):
      num = board[r][c]
      if num == '.':
        continue
      box_idx = (r//3)*3 + (c//3)
      if num in row[r] or num in col[c] or num in boxes[box_idx]:
        return False
  row[r].add(num)
  col[c].add(num)
  boxes[box_idx].add(num)
  return True
