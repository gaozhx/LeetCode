# import numpy as np
# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows==1:
#             return s
        
#         serial=[]
#         down=True
#         row=1
#         for i in range(len(s)):
#             if down:
#                 serial.append(row)
#                 row+=1
#                 if row>numRows:
#                     down=False
#                     row-=2
#             else:
#                 serial.append(row)
#                 row-=1
#                 if row<1:
#                     down=True
#                     row+=2
#         serial=np.asarray(serial)
#         indices=np.argsort(serial,kind="stable")
#         res=""
#         for i in indices:
#             res+=s[i]
#         return res

"""
下面为改进版本
"""
import numpy as np
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        index=locals()
        for i in range(numRows):
            index[i+1]=""
        serial=[]
        down=True
        row=1
        for i in range(len(s)):
            if down:
                index[row]+=str(s[i])
                row+=1
                if row>numRows:
                    down=False
                    row-=2
            else:
                index[row]+=str(s[i])
                row-=1
                if row<1:
                    down=True
                    row+=2
        
        res=""
        for i in range(numRows):
            res+=index[i+1]
        return res
if __name__=="__main__":
    s = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
    numRows = 2
    so=Solution()
    print(so.convert(s,numRows))