# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/ 

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end= 0, len(nums)-1
        while start<=end:
            mid= (start+end)//2
            if nums[mid] == target:
                return True
            # left sorted array
            if nums[start]< nums[mid]:
                if nums[start] > target or nums[mid] < target:
                    start= mid+1
                else:
                    end= mid-1
            # right sorrted array
            elif nums[start] > nums[mid]:
                if nums[end] < target or nums[mid] > target:
                    end= mid - 1
                else:
                    start= mid+1
            # Handle Duplicates if nums[start] == nums[mid] == nums[end]:
            else:
                start += 1
        return False
