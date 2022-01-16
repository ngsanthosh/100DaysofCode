class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points is None:
            return 0
        
        points.sort()
        arrow=1
        currEnd=points[0][1]
        
        for i in points[1:]:
            if(i[0]<=currEnd):
                currEnd=min(i[1],currEnd)
            else:
                arrow+=1
                currEnd=i[1]
        return arrow
                