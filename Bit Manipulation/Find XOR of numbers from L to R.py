# https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1

class Solution:
    def findXOR(self, l, r):
        return self.XORtillN(l-1) ^ self.XORtillN(r)
        
    def XORtillN(self, n):
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n + 1
        if n % 4 == 3:
            return 0
        return n
