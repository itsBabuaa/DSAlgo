# https://leetcode.com/problems/merge-sorted-array/description/
'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.
[better]
Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
Merge both the arrays into a single array sorted in non-decreasing order.
The final sorted array should be stored inside the array nums1 and it should be done in-place.
nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
nums2 has a length of n.
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        size= m+n-1
        m -= 1
        n -= 1
        while m>=0 and n>=0:
            if nums1[m] >= nums2[n]:
                nums1[size]= nums1[m]
                m -= 1
            else:
                nums1[size]= nums2[n]
                n -= 1
            size -= 1

        while n>=0:
            nums1[size] = nums2[n]
            n, size= n-1, size-1
