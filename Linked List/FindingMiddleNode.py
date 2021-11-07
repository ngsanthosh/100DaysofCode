# Python Program to find the middle node of the linked list.

'''Algo:
We first have two pointers pointing on head node, and the pointer double goes two steps ++ 
at a time and the pointer
single does one step ++ at a time. So this keeps on happening till the double pointer is null 
or next of double pointer is null. Finally the single pointing node will be the middle element 
obviously'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        double = single = head
        
        while(double and double.next):
            double=double.next.next
            single=single.next
        return single
        