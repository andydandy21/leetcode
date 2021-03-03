#Reverse Integer


class Solution:
    def reverse(self, x: int) -> int:
        y = 1 if x>=0 else -1
        r = [-2**31,2**31-1]
        rev = int(str(abs(x))[::-1])*y 
        solution = rev if r[0]<rev<r[1] else 0
        return solution