class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llList = linkedList()
first = True
second = True
prevNode = node(None)
stopMsg = ''
while stopMsg != 'n':
    nodeValue = input("Enter node value: ")
    if first:
        llList.head = node(nodeValue)
        first = False
    elif second:
        nextNode = node(nodeValue)
        llList.head.next = nextNode
        nextNode.prev = llList.head
        prevNode = nextNode
        second = False
    else:
        nextNode = node(nodeValue)
        prevNode.next = nextNode
        nextNode.prev = prevNode
        prevNode = nextNode
    stopMsg = input ("Do you want to continue y/n: ")


#Check Plaindorme

def checkPalindrome(headNode):
    temp = headNode
    runnerNode = headNode
    stack = []
    while runnerNode and runnerNode.next:
        stack.append(temp.data)
        temp = temp.next
        runnerNode = runnerNode.next.next
    if not runnerNode.next:
        temp = temp.next
    while temp:
        popValue = int(stack.pop())
        if int(temp.data) != popValue:
            return False
        temp = temp.next
    return True
        
llList.printList()
print("After checkPalindrome : ")
#print(llList.head.data , llList.head.next.data)
print(checkPalindrome(llList.head))