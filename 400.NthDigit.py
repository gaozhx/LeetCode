class Solution:
    def findNthDigit(self, n: int) -> int:
        num_last=0
        num_now=0
        for i in range(1,11):
            num_now=(10**i-10**(i-1))*i+num_last
            if n<=num_now:
                zhengchu=(n-num_last)//i
                mod=(n-num_last)%i
                data=10**(i-1)-1+zhengchu
                if mod==0:
                    return data%10
                else:
                    data=data+1
                    return data//(10**(i-mod))%10
            num_last=num_now
                
        
        
if __name__=="__main__":
    n=10
    so=Solution()
    print(so.findNthDigit(n))