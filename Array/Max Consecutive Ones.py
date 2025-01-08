# https://leetcode.com/problems/max-consecutive-ones/description/
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if count > max1:
                    max1 = count
                count = 0
        return max(max1, count)
