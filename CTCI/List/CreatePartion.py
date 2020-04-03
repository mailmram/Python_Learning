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


#Partion My List
def partitonMyList(myList: linkedList, partionValue = 5):
    partitionNode = node(partionValue)
    nextNode = None
    previousNode = None
    temp = myList.head
    while temp:
        if int(temp.data) >= partionValue:           
           if nextNode is None:
               nextNode = node(temp.data)
               nextNode.prev = partitionNode 
               partitionNode.next = nextNode
           else:
               nextNode.next = node(temp.data)
               nextNode.next.prev = nextNode                              
        else:
            #print("List data: ", temp.data)
            if previousNode is None:
                previousNode = node(temp.data)
                partitionNode.prev = previousNode
                previousNode.next = partitionNode
            else:
                previousNode.prev = node(temp.data)
                previousNode.prev.next = previousNode    
        temp = temp.next

    #partitionNode.prev.next = partitionNode.next
    #partitionNode.next.prev = partitionNode.prev

    newListTemp = previousNode
    #print("first Node:" , previousNode.data)
    while newListTemp:
        print(newListTemp.data)
        newListTemp = newListTemp.next


        
llList.printList()
print("After partion : ")
partitonMyList(llList, 5)