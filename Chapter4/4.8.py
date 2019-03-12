#First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
#Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
class Node():
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value
        self.parent = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.inorder = []

    def insert_to_right(self,new_node):

        if self.root == None:
            self.root = new_node

        else:
            current = self.root
            while(current.value is not None):
                if(current.right == None):
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right

    def insert_to_left(self,new_node):

        if self.root == None:
            self.root = new_node

        else:
            current = self.root
            while(current.value is not None):
                if(current.left == None):
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left


    def find_firstcom_ancestor(self,node1,node2):
        n1_P = node1.parent
        n2_P = node2.parent
        while(n1_P!= n2_P and n2_P!=self.root and n1_P!=self.root):
            n1_P = n1_P.parent
            n2_P = n2_P.parent
        return n2_P.value

    def in_order_traversal(self,node):
        if(node != None):
            self.in_order_traversal(node.left)
            self.inorder.append(node)
            self.in_order_traversal(node.right)

    def print_inorder(self):
        for i in self.inorder:
            print(i.value)


def main():
    bst = BinaryTree()
    node1 = Node(6)
    node2 = Node(9)
    node3 = Node(5)
    node4 = Node(4)
    node5 = Node(18)
    node6 = Node(8)

    bst.insert_to_right(node1)
    bst.insert_to_left(node2)
    bst.insert_to_left(node3)
    bst.insert_to_left(node4)
    bst.insert_to_right(node5)
    bst.insert_to_right(node6)
    bst.in_order_traversal(bst.root)
    #bst.print_inorder()
    print(bst.find_firstcom_ancestor(node5,node6))


if __name__ == '__main__':
    main()
