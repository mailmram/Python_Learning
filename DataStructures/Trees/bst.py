class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, root, insertnode):
        if root is None:
            root = insertnode
        else:
            if root.data < insertnode.data:
                if root.right is None:
                    root.right = insertnode
                else:
                    self.insert(root.right, insertnode)
            else:
                if root.left is None:
                    root.left = insertnode
                else:
                    self.insert(root.left, insertnode)
    
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

rootNode = node(50)
rootNode.insert(rootNode, node(49))
rootNode.insert(rootNode, node(51))
rootNode.insert(rootNode, node(10))
rootNode.insert(rootNode, node(5))
rootNode.insert(rootNode, node(4))
rootNode.insert(rootNode, node(6))
rootNode.insert(rootNode, node(11))
rootNode.insert(rootNode, node(13))
rootNode.insert(rootNode, node(8))
rootNode.insert(rootNode, node(7))
rootNode.insert(rootNode, node(100))
rootNode = rootNode.deleteNode(20, rootNode)
rootNode.inOrderTraversal(rootNode)