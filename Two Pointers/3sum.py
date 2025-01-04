# https://leetcode.com/problems/3sum/
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1
        return res
