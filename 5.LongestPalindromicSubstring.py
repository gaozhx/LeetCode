class Solution(object):
    def longestPalindrome(self, s):
        """
        使用扩展中心算法
        :type s: str
        :rtype: str
        """
        max_range=0
        range_index=()
        for i in range(len(s)):
            left=i
            right=i
            num_range,temp_range=self.cal_range(s,left,right)
            if num_range>max_range:
                max_range=num_range
                range_index=temp_range
            if i!=len(s)-1 and s[i]==s[i+1]:
                left=i
                right=i+1
                num_range,temp_range=self.cal_range(s,left,right)
                if num_range>max_range:
                    max_range=num_range
                    range_index=temp_range
        return s[range_index[0]:range_index[1]+1]
    def cal_range(self,s,left,right):
        num_range=1 if left==right else 2
        while(True):
                if left-1<0 or right+1 >len(s)-1:
                    break
                if s[left-1]==s[right+1]:
                    left=left-1
                    right=right+1
                    num_range+=2
                else:
                    break
        return num_range,(left,right)

if __name__=="__main__":
    so=Solution()
    print(so.longestPalindrome("cbbd"))
    print("hhhh")
        