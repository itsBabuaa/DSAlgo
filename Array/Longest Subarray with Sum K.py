# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
'''
Given an array arr[] containing integers and an integer k,
your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k.
If there is no subarray with sum equal to k, return 0.
'''

class Solution:
    def longestSubarray(self, nums, k):  
        # code here
        hm= {0:1}
        summ= 0
        maxLen= 0
        for i in range(len(nums)):
            summ += nums[i]
            target= summ - k
            if summ== k:
                maxLen= max(maxLen, i+1)
            if target in hm:
                length = i - hm[target]
                maxLen = max(maxLen, length)
            if summ not in hm:
                hm[summ] = i

        return maxLen
