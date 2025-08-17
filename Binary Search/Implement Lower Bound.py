# https://www.geeksforgeeks.org/problems/implement-lower-bound/1

class Solution:
    def lowerBound(self, nums, x):
        # code here
        res= len(nums)
        start, end= 0, res-1

        while start <= end:
            mid= (start+ end)//2
            if nums[mid]>=x:
               res= mid
               end= mid-1
            else:
                start= mid+1
        return res
