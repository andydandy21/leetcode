#Regular Expression Matching


def regex(s,p):
    if not p:
        return p==s
    else:
        if not s:
            if p[-1] == '*':
                return regex(s, p[:-2])
            return False
        
        elif p[-1] == s[-1] or p[-1] == ".":
            return regex(s[:-1], p[:-1])
        
        elif p[-2:] == '.*':
            if len(p)>2:
                if not s:
                    return False
                else:
                    if p[-4:-2] == '.*':
                        return regex(s,p[:-2])
                    elif p[-3] == s[-1] or p[-3]=='.':
                        if regex(s,p[:-2]):
                            return regex(s,p[:-2])
                        else:
                            return regex(s[:-1], p)
                    elif p[-3] == '*':
                        if regex(s,p[:-2]):
                            return regex(s,p[:-2])
                        else:
                            return regex(s[:-1], p)
                    else:
                        return regex(s[:-1],p)
            else:
                return True
        
        elif p[-1] == '*':
            if p[-2] == s[-1]:
                if regex(s[:-1], p[:-2]):
                    return regex(s[:-1], p[:-2])
                else:
                    if regex(s[:-1],p):
                        return regex(s[:-1],p)
                    else:
                        return regex(s,p[:-2])
                        
            else:
                return regex(s, p[:-2])
        
        else:
            return False
            
            
            
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return regex(s,p)



# Easier to read

def regex_dot_star(s,p):
    if len(p)<=2:
        return True
    else:
        if p[-4:-2] == '.*':
            return regex_dot_star(s,p[:-2])
        elif p[-3] == s[-1] or p[-3]=='.':
            if regex(s,p[:-2]):
                return regex(s,p[:-2])
            else:
                return regex_dot_star(s[:-1], p)
        elif p[-3] == '*':
            if regex(s,p[:-2]):
                return regex(s,p[:-2])
            else:
                return regex_dot_star(s[:-1], p)
        else:
            return regex_dot_star(s[:-1],p)

def regex_star(s,p):
    if p[-2] != s[-1]:
        return regex(s, p[:-2])
    else:
        if regex(s[:-1], p[:-2]):
            return regex(s[:-1], p[:-2])
        else:
            if regex(s[:-1],p):
                return regex(s[:-1],p)
            else:
                return regex(s,p[:-2])          
            

def regex(s,p):
    if not p:
        return p==s
    else:
        if not s:
            if p[-1] == '*':
                return regex(s, p[:-2])
            return False
        
        elif p[-1] == s[-1] or p[-1] == ".":
            return regex(s[:-1], p[:-1])
        
        elif p[-2:] == '.*':
            return regex_dot_star(s,p)
        
        elif p[-1] == '*':
            return regex_star(s,p)
        
        else:
            return False