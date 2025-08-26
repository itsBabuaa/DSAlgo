# https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

class Solution:
    def __init__(self):
        self.res= []

    def helper(self, mat, r, c, dir, n):
        if r == n-1 and c == n-1:
            self.res.append(dir)
            return

        if mat[r][c] == 0:
            return

        mat[r][c] = 0 # marking as vistied

        if r > 0:
            self.helper(mat, r-1, c, dir + 'U', n)
        if c > 0:
            self.helper(mat, r, c-1, dir + 'L', n)
        if r < n-1:
            self.helper(mat, r+1, c, dir + 'D', n)
        if c < n-1:
            self.helper(mat, r, c+1, dir + 'R', n)

        mat[r][c] = 1 # unmark

    def ratInMaze(self, maze):
        # code here
        n= len(maze)
        self.res= []

        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return self.res

        self.helper(maze, 0, 0, '', n)
        self.res.sort()

        return self.res
