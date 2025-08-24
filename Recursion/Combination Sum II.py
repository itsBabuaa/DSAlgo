# https://leetcode.com/problems/combination-sum-ii/description/

class Solution:
    def helper(self, idx, arr, target, curr, ans):
        if target == 0:
            ans.append(curr.copy())
            return
        if target < 0 or idx == len(arr):
            return

        curr.append(arr[idx])
        self.helper(idx+1, arr, target - arr[idx], curr, ans)
        curr.pop()

        # skipping duplicates
        while idx+1 < len(arr) and arr[idx] == arr[idx + 1]:
            idx += 1
            if arr[idx] > target:
                return
        self.helper(idx+1, arr, target, curr, ans)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.helper(0, candidates, target, [], ans)
        return ans
