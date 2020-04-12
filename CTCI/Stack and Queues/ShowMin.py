class Stack:
    class node:
        def __init__(self,data):
            self.next = None
            self.data = data
    
    def __init__(self):
        self.top = None
        self.min = None
    
    def push(self, data: node):
        if self.top == None:
            self.top = data
            self.min = data
        else:
            self.top.next = data
            self.top = self.top.next
            if(self.min.data > data.data):
                self.min = data
    
    def showMin(self):
        print("Minimum Value", self.min.data)
    
    def pop(self):
        if self.top == None:
            print("Stack Empty")
        else:
            lastElm = self.top.data
            self.top = self.top.next
            print("Popped Item", lastElm)

    def peek(self):
        if self.top == None:
            print("Stack Empty")
        else:
            print("Peek Item", self.top.data)
    
    def itreateStack(self):
        res = []
        temp = self.top
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        print('<-'.join(res))

myStack = Stack()
myStack.push(myStack.node(5))
myStack.push(myStack.node(6))
myStack.push(myStack.node(7))
myStack.push(myStack.node(1))
myStack.showMin()
