import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None 

#LL Implementations
class LinkedList: 

    def __init__(self): 
        self.head = None


    def display(self):
        temp = self.head 
        while (temp.next is not self.head): 
            print("{} ->".format(temp.info)),
            temp = temp.next
        print("{} ->".format(temp.info)),
        print("NULL")
    def insert_at_beg(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            self.head.next=self.head
            return
        self.p=self.head
        while self.p.next is not self.head:
            self.p=self.p.next
        self.temp.next=self.head
        self.p.next=self.temp
        self.head=self.temp
    def insert_at_end(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            self.head.next=self.head
            return
        self.p=self.head
        while self.p.next is not self.head:
            self.p=self.p.next
        self.p.next=self.temp
        self.temp.next=self.head
    def insert_after_given_node(self,data,item):
        self.p=self.head
        while self.p.next is not self.head:
            if self.p.info==item:
                self.temp=node(data)
                self.temp.next=self.p.next
                self.p.next=self.temp
                return
            self.p=self.p.next
        if self.p.info==item:
            self.temp=node(data)
            self.p.next=self.temp
            self.temp.next=self.head
    def delete(self,data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next==self.head:
            if self.head.info==data:
                self.temp=self.head;
                self.head=None
                return
            
            else:
                print("element not found")
                return
        
        if self.head.next.info==data:
            self.temp=self.head.next
            self.head.next=self.temp.next
            return
        self.p=self.head.link
        while(self.p.next is not self.head):
            if(self.p.next.info==data): 
                self.temp=self.p.next
                self.p.next=self.temp.next
                return
            self.p=self.p.next
        
        if(self.head.info==data):    
            self.temp=self.head
            self.p.next=self.head.next
            self.head=self.p
            return
        
#Actual Code
def splitList(head):
    if head==None:
        return 
    slowptr=head
    fastptr=head
    while(fastptr.next != head and fastptr.next.next != head ): 
        fastptr = fastptr.next.next
        slowptr = slowptr.next
    if fastptr.next.next == head: 
            fastptr = fastptr.next
    temp1=head
    if head.next != head: 
        temp2 = slowptr.next
    fastptr.next = slowptr.next
    slowptr.next = head 
    return temp1,temp2
    
if __name__=='__main__':
    llist=LinkedList()
    list1=LinkedList()
    list2=LinkedList()
    
    print("Enter number of elements")
    n=int(input())
    for i in range(n):
        llist.insert_at_end(int(input()))
    
    list1.head,list2.head=splitList(llist.head)
    
    list1.display()
    list2.display()
