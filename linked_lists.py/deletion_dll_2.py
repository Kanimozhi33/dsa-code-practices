def delete_node_without_head(node_to_delete):
    if not node_to_delete:  # If the node is None, return
        return

    # If the node to delete is not the tail
    if node_to_delete.next:
        node_to_delete.next.prev = node_to_delete.prev

    # If the node to delete is not the head
    if node_to_delete.prev:
        node_to_delete.prev.next = node_to_delete.next

    # The node is effectively removed. In Python, memory cleanup is handled by garbage collection.
    