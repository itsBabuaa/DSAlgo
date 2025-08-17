# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end= 0, len(nums)-1
        while start<=end:
            mid= (start+end)//2
            if nums[mid] == target:
                return mid
            # left sorted array
            if nums[start]<= nums[mid]:
                if nums[start] > target or nums[mid] < target:
                    start= mid+1
                else:
                    end= mid-1
            # right sorrted array
            else:
                if nums[end] < target or nums[mid] > target:
                    end= mid - 1
                else:
                    start= mid+1
        return -1
