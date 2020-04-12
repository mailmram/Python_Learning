class queue:
    class node:
        def __init__(self, data):
            self.next = None
            self.data = data
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, node: node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head == None:
            print("Queue Empty")
        else:
            printVal = self.head.data
            self.head = self.head.next
            print("Removed Item", printVal)

    def peek(self):
        if self.head == None:
            print("Queue empty")
        else:
            print("Peek Item", self.head.data)
    
    def printQueue(self):
        res = []
        temp = self.head
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        print('<-'.join(res))

q = queue()
q.enqueue(q.node(5))
q.enqueue(q.node(6))
q.enqueue(q.node(7))
q.enqueue(q.node(8))
q.dequeue()
q.printQueue()
