def reverseListRecursive(self, head):
    if not head or not head.next:
        return head
    reversed_head = self.reverseListRecursive(head.next)  # Reverse the rest of the list
    head.next.next = head  # Make the next node point to the current node
    head.next = None  # Set the current node's next pointer to None
    return reversed_head