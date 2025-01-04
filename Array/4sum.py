# https://leetcode.com/problems/4sum/description/
'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        
        def helper(k, start, target):
            #recursive case
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    helper(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            #base case (2sum in sorted array)
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        helper(4, 0, target)
        return res

# This solution is a general solution for any kSum problem
# we can use nasted for loops as-well which will also take the same n^3 time
