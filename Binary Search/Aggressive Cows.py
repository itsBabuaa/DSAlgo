# https://www.geeksforgeeks.org/problems/aggressive-cows/1

class Solution:
    def aggressiveCows(self, nums, k):
        nums.sort()
        l, r= 0, (nums[-1]-nums[0])
        
        while l<=r:
            mid= (l+r)//2
            if self.helper(nums, k, mid):
                l= mid+1
            else:
                r= mid-1
        return r

    def helper(self, nums, cows, dist):
        lastCow= nums[0]
        cowCnt= 1
        
        for i in range(1, len(nums)):
            if nums[i] - lastCow >= dist:
                cowCnt+= 1
                lastCow= nums[i]
            if cowCnt== cows:
                return True
        return False
