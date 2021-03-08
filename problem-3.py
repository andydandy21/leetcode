#3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        max_length = len(set(s))
        count = 0
        for x in range(len(s)):
            mylist = []
            for y in s[x:]:
                if y not in mylist:
                    mylist.append(y) 
                else: 
                    break 
            count = (len(mylist) if len(mylist) > count else count)
            if count == max_length: break  
        return count


# Recursive Solution
def recursiveSolution(s, solution=0):
  if solution >= len(set(s)):
    return solution
  else:
    for i in range(len(s)):
      if len(s[i:])<=len(set(s[i:])):
        solution = max(solution,len(s[i:]))
        break
    return recursiveSolution(s[:-1], solution)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        return recursiveSolution(s)