# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        for num in nums:
            ones ^= num
        return ones
