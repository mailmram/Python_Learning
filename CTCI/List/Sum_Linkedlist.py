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
            print(temp.data, end = "")
            if temp.next:
                print("->",)
            temp = temp.next


def createLinkedList():
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
    return llList


def sumofListReverse(list1 : linkedList, list2 : linkedList):
    


llList1 = createLinkedList()
llList2 = createLinkedList()
print("List 1" , llList1.printList())
print("List 2" , llList2.printList())