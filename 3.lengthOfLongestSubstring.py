class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        cur_len=0
        max_len=0
        left=0
        look_up=set()
        for i in range(n):
            cur_len+=1
            while(s[i] in look_up):
                look_up.remove(s[left])
                left+=1
                cur_len-=1
            look_up.add(s[i])
            max_len=cur_len if cur_len>max_len else max_len
        return max_len