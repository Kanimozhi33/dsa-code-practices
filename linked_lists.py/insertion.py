def insertion(self,data,head):
    if not head:
        return None
    tail = head

    new_node = Node(data)
    while tail.next != None:
        tail = tail.next
    if tail.prev:
        curr = tail.prev
        curr.next  = new_node
        tail.prev = new_node
        new_node.prev = curr
        new_node.next = tail
        return head
    else:

        new_node.prev = None
        new_node.next = tail
        return head

def insertion_at_k(self,head,k,data):
    if not head:
        return None
    curr = head
    new_node = Node(data)
    count = 1
    if k == 1:
        new_node.prev = None
        new_node.next = head
        head.prev = new_node
        return new_node

    while curr.next !=  None and k!=1:
        count += 1
        if count == k:
            break
        curr = curr.next
    if count == k:
        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node

        curr.prev = new_node
        new_node.next = curr
        return head
