# https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def helper(self, nums, k):
        temp= 0
        for i in nums:
            temp+= math.ceil(i/k)
        return temp
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       maxi= max(piles)
       l, r= 1, maxi
       while l<=r:
        k= (l+r)//2
        total_hr= self.helper(piles, k)
        if total_hr <= h:
            r= k-1
        else:
            l= k+1
       return l
