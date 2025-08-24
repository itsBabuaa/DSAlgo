# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def helper(self, idx, arr, target, ds, res):
        # base case
        if target == 0:
            res.append(ds.copy())
            return
        if idx >= len(arr) or target < 0:
            return
        
        if arr[idx] <= target:
            ds.append(arr[idx])
            self.helper(idx, arr, target - arr[idx], ds, res)
            ds.pop()
        self.helper(idx+1, arr, target, ds, res)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        self.helper(0, candidates, target, [], res)
        return res        
