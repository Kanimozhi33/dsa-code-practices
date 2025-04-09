class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2.pop()


    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2[-1]
        

    def empty(self) -> bool:
        return  not self.stack2 and not self.stack1
    

    
# code in javascript:
# class MyQueue {
#     constructor() {
#        this.stack1 = []; // Stack to hold the elements
#        this.stack2 = []; // Stack to reverse the order of elements
#     }
#     push(x) {
#        this.stact1.push(x)}
#    pop() {
#        if (this.stack2.length === 0) {
#            while (this.stack1.length > 0) {
#                this.stack2.push(this.stack1.pop());
#            }}
#         return this.stack2.length > 0 ? this.stack2.pop() : -1;
#        }  
#    peek(){
#        if (this.stack2.length === 0) {
#            while (this.stack1.length > 0) {   
#                this.stack2.push(this.stack1.pop());
#            }}
#        return this.stack2.length > 0 ? this.stack2[this.stack2.length - 1] : -1;
#        }
#    empty() {
#        return this.stack1.length === 0 && this.stack2.length === 0;
#    }
# }

