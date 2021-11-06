# CODE NOT YET FINALIZED, TEST CASES ARE FAILING
# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        freshoranges=0
        queue = deque()
        for r in range(row):
            for c in range(col):
                if(grid[r][c]==2):
                    queue.append((r,c))
                elif(grid[r][c]==1):
                    freshoranges+=1
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        timetook=-1
        queue.append((-1,-1))
        while queue:
            row, col = queue.popleft()
            if(row==-1):
                timetook+=1
                if queue:
                  queue.append((-1,-1))  #Checkpoint
            else:
                for d in directions:
                    n_row, n_col = row + d[0], col + d[1]
                    if row>n_row>=0 and col>n_col>=0:
                        if grid[n_row][n_col]==1:
                            grid[n_row][n_col]=2
                            freshoranges-=1
                            queue.append((n_row, n_col))
        return timetook if freshoranges==0 else -1 
                            
                            
                            
                        
            
                
            
            
                
        
        