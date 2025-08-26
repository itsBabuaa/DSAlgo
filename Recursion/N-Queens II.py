# https://leetcode.com/problems/n-queens-ii/description/

class Solution:
    def isSafe(self, row, n, colSet, posDia, negDia):
            # Base Case
            if row == n:
                return 1
            
            cnt= 0

            for col in range(n):
                # Skipping if not safe to place
                if col in colSet or (row+col) in posDia or (row-col) in negDia:
                    continue
                
                # Updating Values when safe to place
                colSet.add(col)
                posDia.add(row+col)            
                negDia.add(row-col)

                cnt += self.isSafe(row+1, n, colSet, posDia, negDia)

                colSet.remove(col)
                posDia.remove(row+col)            
                negDia.remove(row-col)
                
            return cnt
    
    def totalNQueens(self, n: int) -> int:
        colSet= set()
        posDia= set() # (row+col) will be same
        negDia= set() # (row-col) will be same

        return self.isSafe(0, n, colSet, posDia, negDia)
