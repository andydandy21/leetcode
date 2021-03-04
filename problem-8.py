#String to Integer (atoi)


class Solution:
    def myAtoi(self, s: str) -> int:
        mystring = ''
        p = 0
        for i in s:
            if i==' ':
                p += 1
            else: 
                break
        for i in s[p:]:
            if i in '-+':
                mystring += i
                p +=1
                break
            else:
                break
        for i in s[p:]:
            if i in '0123456789':
                mystring += i
            else: 
                break
        try:
            solution = int(mystring) if mystring else 0
        except:
            solution = 0
            
        if solution > 2**31-1:
            solution = 2**31-1
        elif solution < -2**31:
            solution = -2**31
        return solution