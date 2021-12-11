class Solution:
    def reverse(self, x: int) -> int:
        sigmol=True
        if x> 2**31-1 or x<-2**31:
            return 0
        if x<0:
            x=-x
            sigmol=False
        
        res=0
        while(x/10!=0):
            res=res*10+x%10
            x=int(x/10)
        
        if sigmol==False:
            res=-res
        if res> 2**31-1 or res<-2**31:
            res=0
        return res
    
if __name__=="__main__":
    x=120
    so=Solution()
    print(so.reverse(x))