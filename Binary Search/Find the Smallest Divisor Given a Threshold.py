# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

class Solution:
    def helper(self, nums, limit):
        summ= 0
        for num in nums:
            summ += math.ceil(num/limit)
        return summ

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r= 1, max(nums)

        if len(nums) > threshold:
            return -1

        while l<=r:
            mid= (l+r)//2
            if self.helper(nums, mid) <= threshold:
                r= mid - 1
            else:
                l= mid + 1
        return l
