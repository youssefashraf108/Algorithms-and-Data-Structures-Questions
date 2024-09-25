#1) Create a tree node left and right pointing to null and 2) Create a binary tree 3) Preorder traversal using recursion
class TreeNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):

        self.root = None
    #2) Create a binary tree
    def createBinaryTree(self):
        first = TreeNode(1)
        second = TreeNode(2)
        third = TreeNode(3)
        fourth = TreeNode(4)
   

        self.root = first
        first.left = second
        first.right = third

        second.left = fourth

    #3) Preorder traversal using recursion
    def preOrder(self,node):
        if node:
            print(node.data, end = " ")
            self.preOrder(node.left)
            self.preOrder(node.right)





if __name__ == "__main__":
    tree = BinaryTree()
    tree.createBinaryTree()
    tree.preOrder(tree.root)
