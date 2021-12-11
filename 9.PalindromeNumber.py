class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        x_revered=0
        while(x>x_revered):
            x_revered=x_revered*10+x%10
            x=x//10
        if x==x_revered:
            return True
        if x<x_revered:
            x_revered=x_revered//10
        return x_revered==x
    
if __name__=="__main__":
    x=0
    so=Solution()
    print(so.isPalindrome(x))