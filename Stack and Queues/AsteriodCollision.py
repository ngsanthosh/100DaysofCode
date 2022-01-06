# https://leetcode.com/problems/asteroid-collision/



# import math
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stok=[]
        for i in asteroids:
            
            
            while stok and i < 0 < stok[-1]:
                if(stok[-1]<abs(i)):
                    stok.pop()
                    continue
                elif(stok[-1]==abs(i)):
                    stok.pop()
                break
                
            else:
                stok.append(i)
        return stok
                
        #     if(i>=0):
        #         stok.append(i)
        #     elif(i<0):
        #         if len(stok)>0:
        #             if stok[-1]<abs(i):
        #                 stok.pop()
        #             elif stok[-1]>abs(i):
        #                 pass
        #             elif stok[-1]==abs(i):
        #                 stok.pop()
        # return stok