



#Method1
def isCircular(head):
    # Code here
    curr=head
    while curr:
        if(curr.next==head):
            return True
        curr=curr.next
    return False


#Method2
def isCircular(head):
    # Code here
    temp = head.next;
    while(temp!=None and temp!=head):
        temp=temp.next;
    return temp==head