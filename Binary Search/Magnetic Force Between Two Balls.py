# https://leetcode.com/problems/magnetic-force-between-two-balls/description/

class Solution:
    def maxDistance(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r= 0, (nums[-1]-nums[0])
        
        while l<=r:
            mid= (l+r)//2
            if self.helper(nums, k, mid):
                l= mid+1
            else:
                r= mid-1
        return r

    def helper(self, nums, k, dist):
        last= nums[0]
        Cnt= 1
        
        for i in range(1, len(nums)):
            if nums[i] - last >= dist:
                Cnt+= 1
                last= nums[i]
            if Cnt== k:
                return True
        return False
