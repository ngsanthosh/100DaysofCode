
#HARD
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        
        stack=[]
        MaxArea=0
        
        i=0
        while i<len(heights):
            if (not stack) or (heights[i]>=heights[stack[-1]]):
                stack.append(i)
                i+=1
            else:
                topp=stack.pop()
                currArea=heights[topp]*(i-stack[-1]-1 if stack else i)
                MaxArea=max(currArea,MaxArea)
                
        while stack:
                topp=stack.pop()
                currArea=heights[topp]*((i - stack[-1] - 1) if stack else i)
                MaxArea=max(currArea,MaxArea)
                
        return MaxArea
            
                
                
                
        
        