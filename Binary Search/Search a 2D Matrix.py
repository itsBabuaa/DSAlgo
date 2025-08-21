# https://leetcode.com/problems/search-a-2d-matrix/description/

# Solution 1 no maths
# Time Complexity:O(log(rows)) for finding the row and O(log(cols)) for searching in the row, thus O(log(rows) + log(cols)).
# Space Complexity:O(1) because it uses a constant amount of extra space.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows= len(matrix)
        cols= len(matrix[0])
        # search the row containing target
        top, bot= 0, rows - 1
        while top<= bot:
            row= (top+bot) // 2
            if target < matrix[row][0]:
                bot= row - 1
            elif target > matrix[row][-1]:
                top= row + 1
            else:
                break

        if not (top <= bot):
            return False

        # searching in row
        l, r= 0, cols-1
        while l<=r:
            mid= (l+r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l= mid + 1
            else:
                r= mid - 1
                
        return False

# Solution 2 with maths 
# Time Complexity:The time complexity is O(log(m*n)) due to the binary search.
# Space Complexity:The space complexity is O(1) because it uses a constant amount of extra space.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = m*n - 1
        while low <=  high:
            mid = (low + high)//2
            row = mid // m
            column = mid % m
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
  '''
