import numpy as np
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_=np.array(score)
        indices=np.argsort(score_)[::-1]
        res=["0"]*len(indices)
        for i in range(len(indices)):
            if i==0:
                res[int(indices[i])]="Gold Medal"
            elif i==1:
                res[int(indices[i])]="Silver Medal"
            elif i==2:
                res[int(indices[i])]="Bronze Medal"
            else:
                res[int(indices[i])]=str(i+1)
        return res