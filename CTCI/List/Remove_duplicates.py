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


#Remove Duplicates
def removeDuplicates(myList : linkedList):
    removeDupDict = dict()
    temp = myList.head
    while temp:
            removeDupDict[temp.data] = 0
            temp = temp.next
    print("After removing duplicates : " ,removeDupDict.keys())

llList.printList()
removeDuplicates(llList)
llList.printList()