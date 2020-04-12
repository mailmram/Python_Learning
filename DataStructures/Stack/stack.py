
class stack:
    class node:
        def __init__(self,data):
            self.next = None
            self.data = data
    
    def __init__(self):
        self.top = None

    def push(self,node: node):
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

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

myStack = stack()
myStack.push(myStack.node(5))
myStack.push(myStack.node(6))
myStack.push(myStack.node(7))
myStack.itreateStack()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.peek()
    
