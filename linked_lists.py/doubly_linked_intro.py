# A doubly linked list is a type of data structure in which each element, called a node, is connected to both its previous and next node. Here's a breakdown of how it works:

# Structure: Each node in a doubly linked list contains three parts:

# Data: Stores the value or information.

# Prev Pointer: Points to the previous node in the list.

# Next Pointer: Points to the next node in the list.

# Navigation: Unlike a singly linked list (where you can only move forward), a doubly linked list allows you to traverse in both directions—forward and backward—using the next and previous pointers, respectively.

# Insertion:

# At the Beginning: Update the prev pointer of the current first node to point to the new node. Then, set the new node's next pointer to the current first node and make the new node the head of the list.

# At the End: Update the next pointer of the current last node to point to the new node. Then, set the new node's prev pointer to the current last node and update it as the new last node.

# In the Middle: Adjust the next pointer of the previous node and the prev pointer of the next node to point to the new node, and update the new node's pointers accordingly.

# Deletion:

# From the Beginning: Make the second node the new head and set its prev pointer to null.

# From the End: Make the second-to-last node the new tail and set its next pointer to null.

# From the Middle: Adjust the next and prev pointers of the neighboring nodes to bypass the node being removed.

# Applications: Doubly linked lists are used in scenarios where forward and backward traversal is required, like:

# Implementation of a browser's back and forward navigation.

# Undo and redo operations in text editors.

# Building a LRU (Least Recently Used) cache.
