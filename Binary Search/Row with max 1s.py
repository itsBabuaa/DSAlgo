# https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

class Solution:
    def lowerBound(self, arr, cols, x):
        l, r= 0, cols-1
        lb= cols
        while l<=r:
            mid= (l+r)//2
            if arr[mid] >= x:
                lb= mid
                r= mid-1
            else:
                l= mid+1
        return lb
                
    def rowWithMax1s(self, mat):
        # code here
        idx= -1
        maxxCnt= 0
        rows= len(mat)
        cols= len(mat[0])

        for row in range(rows):
            cnt= cols - self.lowerBound(mat[row], cols, 1)
            if cnt > maxxCnt:
                maxxCnt= cnt
                idx= row
                
        return idx
