# https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]
        lenn= len(nums)

        def dfs(idx):
            if idx >=lenn:
                res.append(curr.copy())
                return

            #pick
            curr.append(nums[idx])
            dfs(idx+1)

            #not pick
            curr.pop()
            dfs(idx+1)

        dfs(0)
        return res
