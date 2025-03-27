# https://leetcode.com/problems/climbing-stairs/description/
'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

# Memoization Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.helper(n, dp)

    def helper(self, n, dp):
        if n <= 1:
            return 1
        elif dp[n] != -1:
            return dp[n]

        dp[n] = self.helper(n-1, dp) + self.helper(n-2, dp)
        return dp[n]

  # Tabulation Solution
  class Solution:
    def climbStairs(self, n: int) -> int:        
        dp = [-1] * (n+1)

        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


# Space Optimized Solution
class Solution:
    def climbStairs(self, n: int) -> int:        
        one, two = 1, 1

        for i in range(2, n+1):
            temp = one
            one = one + two
            two = temp

        return one
