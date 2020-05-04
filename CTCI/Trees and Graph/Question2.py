class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class bst:
    def __init__(self, root):
        if root is None:
            self.root = None
        else:
            self.root = node(root)

    def insert(self, insertnode):
        if self.root is None:
            self.root = insertnode
        else:
            if self.root.data < insertnode.data:
                if self.root.right is None:
                    self.root.right = insertnode
                else:
                    self.root = self.root.right
                    self.insert(insertnode)
            else:
                if self.root.left is None:
                    self.root.left = insertnode
                else:
                    self.root = self.root.left
                    self.insert(insertnode)
                    

    def traverse(self):
        self.inOrderTraversal(self.root)
    
    def inOrderTraversal(self, node):
        if node is not None:
            self.inOrderTraversal(node.left)
            print(node.data)
            self.inOrderTraversal(node.right)
    
    def preOrderTraversal(self, node):
        if node is not None:
            print(node.data)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)
    
    def postOrderTraversal(self, node):
        if node is not None:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.data)
    
    def deleteNode(self, searchNode, rootNode):
        if rootNode is not None:
            if rootNode.data == searchNode:
                if rootNode.left is None:
                    returnNode = rootNode.right
                    rootNode = None
                    return returnNode
                elif rootNode.right is None:
                    returnNode = rootNode.left
                    del rootNode
                    return returnNode
                else:
                    succesorNode = rootNode.right
                    while succesorNode.left:
                        succesorNode = succesorNode.left
                    print(succesorNode.data)
                    rootNode.data = succesorNode.data
                    rootNode.right = self.deleteNode(succesorNode.data,rootNode.right)
            elif rootNode.data < searchNode:
                rootNode.right = self.deleteNode(searchNode, rootNode.right)
            elif rootNode.data > searchNode:
                rootNode.left = self.deleteNode(searchNode, rootNode.left)
        return rootNode

    def height(self, root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right))+1


myArray = [1,2,3,4,5,6,7,8,9,10]
#myBst.traverse()
def minHeight(myBst, myArray, start, end):
    mid = int((start + end)/2)
    myBst.insert(node(myArray[mid]))
    myBst.traverse()
    myBst = minHeight(myBst, myArray, start, 3)  
    #myBst = minHeight(myBst, myArray, mid+1, end)
    return myBst
myBst = bst(None)
myBst = minHeight(myBst, myArray, 0, 9)
# rootNode = node(50)
# myBst = bst(50)
# myBst.insert(rootNode, node(49))
# myBst.insert(rootNode, node(51))
# myBst.insert(rootNode, node(10))
# myBst.insert(rootNode, node(5))
# myBst.insert(rootNode, node(4))
# myBst.insert(rootNode, node(6))
# myBst.insert(rootNode, node(11))
# myBst.insert(rootNode, node(13))
# myBst.insert(rootNode, node(8))
# myBst.insert(rootNode, node(7))
# myBst.insert(rootNode, node(100))
# myBst.inOrderTraversal(rootNode)
# print(myBst.height(rootNode)) 