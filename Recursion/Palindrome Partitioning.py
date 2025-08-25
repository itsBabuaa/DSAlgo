# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def isPali(self, start, end, arr):
        while start <= end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True

    def helper(self, idx, arr, curr, ans):
        if idx == len(arr):
            ans.append(curr[:])
            return

        for i in range(idx, len(arr)):
            if self.isPali(idx, i, arr):
                curr.append(arr[idx:i+1])
                self.helper(i+1, arr, curr, ans)
                curr.pop()

    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        self.helper(0, s, [], ans)
        return ans
