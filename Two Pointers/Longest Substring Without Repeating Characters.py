# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
Given a string s, find the length of the longest substring
without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pre_idx = {}
        length = 0
        maxLen = 0
        l = 0
        for r in range(len(s)):
            i = pre_idx.get(s[r], -1)
            if l <= i:
                l = i + 1
            length = r - l + 1
            maxLen = max(maxLen, length)
            pre_idx[s[r]] = r
        return maxLen
