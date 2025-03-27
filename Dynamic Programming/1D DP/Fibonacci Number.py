# https://leetcode.com/problems/fibonacci-number/description/
'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
'''

# Memoization Solution
class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.fibHelper(n, dp)

    def fibHelper(self, n: int, dp: list) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif dp[n] != -1:
            return dp[n]
        
        dp[n] = self.fibHelper(n-1, dp) + self.fibHelper(n-2, dp)
        return dp[n]
#Time: O(N)
#Space: O(N) + O(N) ≈ O(N)

# Tabulation Solution
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        dp = [-1] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
#Time: O(N)
#Space: O(N)
