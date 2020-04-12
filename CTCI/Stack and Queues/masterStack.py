
myMasterStack = []
class stack:
    class node:
        def __init__(self,data):
            self.next = None
            self.data = data
    
    def __init__(self):
        self.top = None
        self.len = 0

    def push(self,node: node):
        if self.top == None:
            self.top = node
            self.len = self.len + 1
        else:
            print(self.len)
            if self.len == 5:
                myMasterStack.append(self.top)
                self.len =0
                self.top = None
                self.top = node
            else:
                node.next = self.top
                self.top = node
                self.len =  self.len + 1

    def pop(self):
        if self.top == None:
            print("Stack Empty")
        else:
            lastElm = self.top.data
            self.top = self.top.next
            self.len = self.len - 1
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



myStack = stack()
myStack.push(myStack.node(5))
myStack.push(myStack.node(6))
myStack.push(myStack.node(7))
myStack.push(myStack.node(5))
myStack.push(myStack.node(6))
myStack.push(myStack.node(7))
myStack.push(myStack.node(5))
myStack.push(myStack.node(6))
myStack.push(myStack.node(7))
myStack.itreateStack()
myStack.peek()
print(myMasterStack[0])
