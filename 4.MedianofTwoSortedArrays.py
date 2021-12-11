class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)>len(nums2):
            return Solution().findMedianSortedArrays(nums2,nums1)
        len1=len(nums1)
        len2=len(nums2)
        left=0
        right=len1
        mid=int((len1+len2+1)/2)
        while left<=right:
            x1=int(left+right)/2
            x2=mid-x1
            if x2!=len2 and x1!=0 and nums1[x1-1]>nums2[x2]:
                right = x1 - 1
            elif x1!=len1 and x2!=0 and nums1[x1]<nums2[x2-1]:
                left=x1+1
            else:
                maxleft=0
                if x1==0:
                    maxleft=nums2[x2-1]
                elif x2==0:
                    maxleft=nums1[x1-1]
                else:
                    maxleft=max(nums1[x1-1],nums2[x2-1])
                if (len1+len2)%2==1:
                    return maxleft
                minright=0
                if x1==len1:
                    minright=nums2[x2]
                elif x2==len2:
                    minright=nums1[x1]
                else:
                    minright=min(nums1[x1],nums2[x2])
                return (maxleft+minright)/2.0

