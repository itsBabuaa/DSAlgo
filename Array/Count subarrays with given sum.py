# https://leetcode.com/problems/subarray-sum-equals-k/description/
'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm= {0:1}
        res= 0
        summ= 0
        for i in range(len(nums)):
            summ += nums[i]
            target= summ - k
            if target in hm:
                res += hm[target]
            if summ in hm:
                hm[summ] += 1
            else:
                hm[summ] = 1

        return res
