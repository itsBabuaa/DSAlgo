# https://leetcode.com/problems/candy/
'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [1] * n

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                arr[i] = max(arr[i], arr[i+1] + 1)
        return sum(arr)

# Time: O(n^2)
# Space: O(1)
