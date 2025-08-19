# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

class Solution:
    def minDays(self, nums: List[int], m: int, k: int) -> int:
        if k*m > len(nums):
            return -1
        l, r= min(nums), max(nums)
        while l<=r:
            mid= (l+r)//2
            if self.isPossible(nums, k, m, mid):
                r= mid-1
            else:
                l= mid+1
        return l

    def isPossible(self, nums, k, m, day):
        cnt=0
        bouquet=0
        for i in nums:
            if i<=day:
                cnt+=1
            else:
                bouquet+= cnt//k
                cnt= 0
        bouquet+= cnt//k
        return bouquet >= m
