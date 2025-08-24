# https://leetcode.com/problems/combination-sum-iii/description/

class Solution:
    def helper(self, start, k, n, curr, ans):
        if len(curr) == k and n == 0:
            ans.append(curr.copy())
            return
        if n < 0 or len(curr) > k:
            return

        for idx in range(start, 10):
            if idx > n:
                break
            else:
                curr.append(idx)
                self.helper(idx+1, k, n-idx, curr, ans)
                curr.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans= []
        self.helper(1, k, n, [], ans)
        return ans
