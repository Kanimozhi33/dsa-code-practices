# A linked list (LL) node 
# to store a queue entry 
# error :runtime error:
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.rear = None
        self.front = None
    #Function to push an element into the queue.
    def push(self, item): 
        temp = Node(item)
        if self.front == None:
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
         #Add code here
    
    #Function to pop front element from the queue.
    def pop(self):
        if self.front is None:
            return -1
        else:
            res= self.front.data
            self.front = self.front.next
            if self.front== None:
                self.rear=None
            return res
         #add code here



# The following code is a JavaScript implementation of a queue using a linked list.
# class Node {
#     constructor(data) {
#         this.data = data;
#         this.next = null;
#     }
# }

# class MyQueue {
#     constructor() {
#         this.front = null; // Points to the front of the queue
#         this.rear = null;  // Points to the rear of the queue
#     }

#     // Function to push an element into the queue
#     push(item) {
#         const newNode = new Node(item); // Create a new node with the given item
#         if (this.front === null) {
#             // If the queue is empty, both front and rear point to the new node
#             this.front = this.rear = newNode;
#         } else {
#             // Attach the new node at the rear and update the rear pointer
#             this.rear.next = newNode;
#             this.rear = newNode;
#         }
#     }

#     // Function to pop the front element from the queue
#     pop() {
#         if (this.front === null) {
#             // If the queue is empty
#             return -1;
#         }
#         const poppedData = this.front.data;
#         this.front = this.front.next; // Move the front pointer to the next node
#         if (this.front === null) {
#             // If the queue becomes empty, set rear to null
#             this.rear = null;
#         }
#         return poppedData;
#     }
# }

