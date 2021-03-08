#5. Longest Palindromic Substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        solution = ''
        if len(s)<=1 or len(set(s))<=1:
            return s
        else:
            for x in range(len(s),-1,-1): 
                if len(solution)>x: break
                for y in range(x): 
                    mystring = s[y:x]
                    if mystring == mystring[::-1]: break
                solution = mystring if len(mystring)>=len(solution) else solution
            return solution


# Recursive Solution
def longestPalindrome(s, solution=''):
    if len(solution)>=len(s):
        return solution
    else:
        for i in range(len(s)):
          test = s[i:]
          if test == test[::-1] and len(test)>len(solution):
            return longestPalindrome(s[:-1], test)
        return longestPalindrome(s[:-1], solution)