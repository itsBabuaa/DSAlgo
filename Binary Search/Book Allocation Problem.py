# https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitPossible(self, nums, k, maxi):
        subArrCnt, summ= 1, 0
        for num in nums:
            if maxi >= (summ + num):
                summ+= num
            else:
                summ= num
                subArrCnt+= 1
            if subArrCnt > k or num > maxi:
                return False
        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        l, r= max(nums), sum(nums)
        while l<=r:
            mid =(l+r)//2
            if self.splitPossible(nums, k, mid):
                r= mid-1
            else:
                l= mid+1
        return l
