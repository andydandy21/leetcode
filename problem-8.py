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


# Recursive Solution
def step1(s):
    if s:
        if s[0] == ' ':
            return step1(s[1:])
        return step2(s)
    else:
        return 0

def step2(s):
    if s[0] == '-' or s[0] == '+':
        return step3(s[1:],s[0])
    return step3(s)

def step3(s,solution=''):
    if s:
        if s[0] in '0123456789':
            return step3(s[1:],solution+s[0])
    return step4(solution)

def step4(solution):
    try:
        if solution:
            if int(solution)>2**31-1:
                return 2**31-1
            elif int(solution)<-2**31:
                return -2**31
            return int(solution)
        return 0
    except:
        return 0

class Solution:
    def myAtoi(self, s: str) -> int:
        return step1(s)