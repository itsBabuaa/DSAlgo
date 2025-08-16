# https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1
'''
Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.
'''

class Solution:
    def subarrayXor(self, nums, k):
        hm= {0:1}
        res= 0
        summ= 0
        for i in range(len(nums)):
            summ ^= nums[i]
            target= summ ^ k
            if target in hm:
                res += hm[target]
            if summ in hm:
                hm[summ] += 1
            else:
                hm[summ] = 1

        return res
