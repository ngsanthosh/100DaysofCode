#Method1
def isCircular(head):
    # Code here
    curr=head
    while curr:
        if(curr.next==head):
            return True
        curr=curr.next
    return False