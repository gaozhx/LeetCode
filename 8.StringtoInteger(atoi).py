import re
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX=2**31-1
        INT_MIN=-2**31
        s=s.lstrip()
        pattern=re.compile(r'^[\+\-]?\d+')
        res=pattern.findall(s)
        res=int(*res)
        return min(max(res,INT_MIN),INT_MAX)
    
    
if __name__=="__main__":
    s="   -42ww98"
    so=Solution()
    print(so.myAtoi(s))