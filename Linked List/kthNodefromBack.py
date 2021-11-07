def kthnode(llist,k):
    temp1=llist.head
    temp2=llist.head
    for i in range(k):
        temp1=temp1.next
    while temp1 is not None:
        temp1=temp1.next
        temp2=temp2.next
    return temp2.info