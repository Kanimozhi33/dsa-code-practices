class MyQueue:
    def __init__(self):
        self.queue = []
    #Function to push an element x in a queue.
    def push(self, x):
         
        #add code here
        self.queue.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if not self.queue:
            return -1
        return self.queue.pop(0)
         
         # add code here
# javascript code:
# class MyQueue {
#     constructor() {
#         this.queue = [];
#     }
#     // Function to push an element x in a queue.
#     push(x) {
#         // add code here
#         this.queue.push(x);
#     }

#     // Function to pop an element from queue and return that element.
#     pop() {
#         if (this.queue.length === 0) {
#             return -1;
#         }
#         return this.queue.shift(); // Removes the first element from the array
#     }
# }
