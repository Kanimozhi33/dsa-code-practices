class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None  

    # Function to push an integer into the stack.
    def push(self, data):
        
        new_node = StackNode(data)
        # Point the new node's next to the current top
        new_node.next = self.top
        # Update the top to the new node
        self.top = new_node

    # Function to remove an item from the top of the stack.
    def pop(self):
        if self.top is None:  # Check if the stack is empty
            return -1
        # Retrieve the data from the top node
        popped_data = self.top.data
        # Update the top to point to the next node
        self.top = self.top.next
        return popped_data
# javascript code:
# class StackNode {
#     constructor(data) {
#         this.data = data;
#         this.next = null;
#     }
# }
# class MyStack {
#     constructor() {
#         this.top = null;
#     }
#     push(data) {
#         const newNode = new StackNode(data);
#         newNode.next = this.top;
#         this.top = newNode;
#     }
#     pop() {
#         if (this.top === null) {
#             return -1;
#         }
#         const poppedData = this.top.data;
#         this.top = this.top.next;
#         return poppedData;
#     }
# }
