# https://leetcode.com/problems/maximum-69-number/submissions/

class Solution:
    def maximum69Number (self, num: int) -> int:
        posCnt= 0
        sixPos= -1
        temp= num

        while temp>0:
            rem= temp % 10

            if rem == 6:
                sixPos= posCnt
            
            temp //= 10
            posCnt += 1

        return (num + 3 * pow(10, sixPos)) if sixPos != -1 else nums
