#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Determine if a Sudoku is valid.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

#Complexity
Time: O(n^2)
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = []
            col = []
            sqr = []
            for j in range(9):
                # validate row
                cell_of_row = board[i][j]
                if cell_of_row != '.':
                    if cell_of_row in row:
                        return False
                    else:
                        row.append(cell_of_row)
                # validate column
                cell_of_col = board[j][i]
                if cell_of_col != '.':
                    if cell_of_col in col:
                        return False
                    else:
                        col.append(cell_of_col)
                # validate square
                cell_of_sqr = board[(i / 3 * 3) + (j / 3)][(i % 3 * 3) + (j % 3)]
                if cell_of_sqr != '.':
                    if cell_of_sqr in sqr:
                        return False
                    else:
                        sqr.append(cell_of_sqr)
        return True

if __name__ == '__main__':
	#board = [[two_dimensional_array],[..],..]
	#solution = Solution()
	#print solution.isValidSudoku(board)

