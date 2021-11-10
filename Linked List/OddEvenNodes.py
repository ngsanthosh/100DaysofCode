# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

            if (not head or not head.next or not head.next.next):
                return head
            
            odd, even=head,head.next
            evenHead=head.next
            
            
            while even and even.next:
                odd.next=even.next
                odd=odd.next
                even.next=odd.next
                even=even.next
            
            odd.next=evenHead
            return head
            