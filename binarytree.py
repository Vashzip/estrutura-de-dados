class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
#Classe para representar uma árvore binária.
    def __init__(self):
        self.root = None
    def insert(self, root, data):
    #Insere um nó na árvore
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    def inorder_traversal(self, root):
    #Percorre a árvore em ordem (Inorder)."""
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

bt = BinaryTree()
raiz = bt.insert(None, 8)
bt.insert(raiz, 4)
bt.insert(raiz, 1)
bt.insert(raiz, 5)
bt.insert(raiz, 9)
bt.insert(raiz, 10)
bt.insert(raiz, 20)
bt.insert(raiz, 2)
bt.inorder_traversal(raiz)