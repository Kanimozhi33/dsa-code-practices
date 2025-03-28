def middleNode(self, head):

    if not head:
        return None
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    mid = (count//2) +1
    temp = head
    while temp:
        
        mid -=1
        
        if mid == 0:
            return temp
        temp = temp.next
        
    return temp