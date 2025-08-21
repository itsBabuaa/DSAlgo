# https://leetcode.com/problems/find-peak-element/description/ 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lenn= len(nums)

        if (lenn == 1):
            return 0
        if (nums[0] > nums[1]):
            return 0
        if (nums[lenn-1] > nums[lenn-2]):
            return lenn - 1
        
        l, r = 0, lenn-1

        while l<r:
            mid= (l+r)// 2
            if nums[mid] < nums[mid+1]:
                l= mid+1
            else:
                r= mid
        return r         
