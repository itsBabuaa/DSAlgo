# https://www.geeksforgeeks.org/problems/check-if-there-exists-a-subsequence-with-sum-k/1

#User function Template for python3

class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        # Code here
        def helper(idx, summ):
            if summ == 0:
                return True
            if summ < 0 or idx == N:
                return False

            return helper(idx + 1, summ - arr[idx]) or helper(idx + 1, summ)
        
        return helper(0, K)
