def deletion_head(self,head):
    if not head:
        return None
    new_head = head.next
    if new_head:

        new_head.prev = None

    return new_head

def deletion_tail(self,head):
    if not head:
        return None
    tail = head
    if not head.next:
        return None
    while tail.next != None:

        tail = tail.next

    prev_node = tail.prev
    prev_node.next = None
    return head


def delete_kth_node(self,head,k):
    if not head:
        return None
    if k <= 0 :
        return head
    count = 1
    curr = head
    if k == 1:
        new_head = head.next
        if new_head:

            new_head.prev = None
        return new_head

    while curr and curr.next:
        count+=1

        if count == k:
            break
        curr = curr.next

    if count == k and curr:
        prev_node = curr.prev
        next_node = curr.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
    return head