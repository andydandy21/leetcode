#5. Longest Palindromic Substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        solution = ''
        if len(s)<=1 or len(set(s))<=1:
            return s
        else:
            for x in range(len(s),-1,-1): 
                if len(solution)>x: break
                mystring = 'ab'
                for y in range(x): 
                    mystring = s[y:x]
                    if mystring == mystring[::-1]: break
                solution = mystring if len(mystring)>=len(solution) else solution
            return solution