#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
            
        
        return count
