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