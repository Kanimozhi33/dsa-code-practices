# while head is given.




def deletion(self,data,head):
    if not self.head:
        return None
    curr = self.head
    while curr:

        if curr.data == data:
            if curr == self.head:

                self.head = curr.next
                curr.next.prev = None
                return self.head
            if curr.next:

                curr.next.prev = curr.prev
            if curr.prev:
                curr.prev.next = curr.next
            return self.data
        curr = curr.next
    return self.head
