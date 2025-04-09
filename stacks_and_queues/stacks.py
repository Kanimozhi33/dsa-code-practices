class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr.append(data)
        
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if not self.arr:
            return -1
        return self.arr.pop()
        
        
# javascript code:
# class MyStack {
#    constructor() {
#        this.arr = [];
#    }
#    //Function to push an integer into the stack.
#    push(data) {
#        //add code here
#        this.arr.push(data);
#    }
#    //Function to remove an item from top of the stack.
#    pop() {
#        //add code here
#        if (this.arr.length === 0) {
#            return -1;
#        }
#        return this.arr.pop();
#    }
# }