# https://practice.geeksforgeeks.org/problems/delete-alternate-nodes/1#

#User function Template for python3

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution: 
    
    
    def deleteAlt(self, head):
        poi=head
        # while poi:
        while poi:
            # try:
                if(poi!=None and poi.next!=None):
                    # print("last",poi.data)
                    # print("last",poi.next.next)
                    poi.next=poi.next.next
                    poi=poi.next
                else:
                    return head
            # except:
            #     return head
            # poi=head
            
        
        #add code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        
        n = int(input())
        arr = list(map(int, input().strip().split()))
        #head = createList(arr, n)
        head = Node(arr[0])
        temp = head
        for i in range(1,len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next

        
        ob = Solution()
        ob.deleteAlt(head)
        
        while head is not None:
            print(head.data,end = " ")
            head = head.next
        print()   
        
# } Driver Code Ends