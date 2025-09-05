# https://leetcode.com/problems/single-number-iii/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        rightmost = xor & -xor
        xor1, xor2 = 0, 0

        for num in nums:
            if rightmost & num:
                xor1 ^= num
            else:
                xor2 ^= num

        return [xor1, xor2] if xor1 < xor2 else [xor2, xor1]    # sorted order
