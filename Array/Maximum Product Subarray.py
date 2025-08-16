# https://leetcode.com/problems/maximum-product-subarray/description/
'''
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx= max(nums)
        pref= suff= 1
        for i in range(len(nums)):
            if pref== 0:
                pref=1
            if suff==0:
                suff=1
            pref *= nums[i]
            suff *= nums[len(nums) - i - 1]
            maxx= max(maxx, pref, suff)
        return maxx
