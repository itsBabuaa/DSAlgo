# https://leetcode.com/problems/longest-consecutive-sequence/description/
'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                cnt = 1
                while (num + cnt) in nums_set:
                    cnt += 1
                longest = max(longest, cnt)
        return longest
