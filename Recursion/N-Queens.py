# https://leetcode.com/problems/n-queens/description/

class Solution:
    def isSafe(self, row, board, n, colSet, posDia, negDia, res):
            # Base Case
            if row == n:
                copy= [''.join(row) for row in board]
                res.append(copy)
                return
            
            for col in range(n):
                # Skipping if not safe to place
                if col in colSet or (row+col) in posDia or (row-col) in negDia:
                    continue
                
                # Updating Values when safe to place
                colSet.add(col)
                posDia.add(row+col)            
                negDia.add(row-col)
                board[row][col]= 'Q'

                self.isSafe(row+1, board, n, colSet, posDia, negDia, res)

                colSet.remove(col)
                posDia.remove(row+col)            
                negDia.remove(row-col)
                board[row][col]= '.'
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet= set()
        posDia= set() # (row+col) will be same
        negDia= set() # (row-col) will be same

        res= []
        board= [['.'] * n for i in range(n)] # Empty Board

        self.isSafe(0, board, n, colSet, posDia, negDia, res)

        return res
