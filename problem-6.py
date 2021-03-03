#ZigZag Conversion    


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=numRows or len(set(s))==1 or numRows==1:
            return s
        else:
            d = {num: '' for num in range(1,numRows+1)}
            x = 1
            mystring = ''                       
            for i in s:
                d[x] += i
                x += 1 if 0<x<numRows and len(d[1]) > len(d[numRows]) else -1        
            for num in range(1,numRows+1):
                mystring += d[num]
            return mystring    