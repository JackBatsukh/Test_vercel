class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self,value):
        self.insert_recursive(self.root,value)

    def insert_recursive(self,node,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        if value < node.value:
            if node.left = Node(value):
                node.left = Node(value)
            else:
                self.insert_recursive(node.left,value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right,value)


    