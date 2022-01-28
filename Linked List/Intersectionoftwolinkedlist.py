#  https://www.youtube.com/watch?v=D0X0BONOQhI&ab_channel=NeetCode

# https://leetcode.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1,l2=headA,headB
        while l1!=l2:
            l1=l1.next if l1 else headB
            l2=l2.next if l2 else headA
        return l2
        
#         tocheck=[]
#         while headA.next is not None:
#             tocheck.append(headA.val)
            
#         while headB.next is not None:
#             if headB.val in tocheck:
#                 return headB.val
#         return None
        
            