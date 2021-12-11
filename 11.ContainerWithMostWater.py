# """[summary]这个代码时间负责度为O(n^2),故换下面的,通过极致例子可以发现两个程序是正确的，但效率大大不同
# """
# class Solution:
#     def maxArea(self, height) -> int:
#         num=len(height)
#         fun=lambda left,right:(right-left)*min(height[left],height[right])
#         left=0
#         right=num-1
#         global_max_container=0
#         flag=True
#         while(flag):
#             flag=False
#             local_max_container,left,right=self.localMaximun(height,left,right,fun)
#             if local_max_container>global_max_container:
#                 global_max_container=local_max_container
#             bigger_num=0
#             for i in range(left+1,right):
#                 if height[i]>min(height[left],height[right]):
#                     bigger_num+=1
#             if bigger_num>=2:
#                 flag=True
#                 for i in range(left+1,right):
#                     if height[i]>min(height[left],height[right]):
#                         left=i
#                         break
#                 for j in range(right-1,left,-1):
#                     if height[j]>min(height[left],height[right]):
#                         right=j
#                         break
#         return global_max_container
        
    
#     def localMaximun(self,height,left,right,fun):
#         flag=True
#         local_max_container=fun(left,right)
#         while(flag):
#             flag=False
#             for i in range(left,right+1):
#                 if height[i]<=height[left]:
#                     continue
#                 if fun(i,right)>local_max_container:
#                     flag=True
#                     local_max_container=fun(i,right)
#                     left=i
#             for j in range(right,left-1,-1):
#                 if height[j]<=height[right]:
#                     continue
#                 if fun(left,j)>local_max_container:
#                     flag=True
#                     local_max_container=fun(left,j)
#                     right=j
#         return local_max_container,left,right

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        num=len(height)
        fun=lambda left,right:(right-left)*min(height[left],height[right])
        left=0
        right=num-1
        max_container=fun(left,right)
        while(left<right):
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            temp_container=fun(left,right)
            max_container=temp_container if temp_container>max_container else max_container
        return max_container
if __name__=="__main__":
    height=[i for i in range(10001)]+[j for j in range(9999,-1,-1)]
    so=Solution()
    print(so.maxArea(height))
        
        