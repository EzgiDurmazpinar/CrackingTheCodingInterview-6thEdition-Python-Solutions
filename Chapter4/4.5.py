#Validate BST: Implement a function to check if a binary tree is a binary search tree.
class Node():
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.inorderarray = []

    def insert_to_right(self,value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node

        else:
            current = self.root
            while(current.value is not None):
                if(current.right == None):
                    current.right = new_node
                    break
                current = current.right

    def insert_to_left(self,value):

        new_node = Node(value)

        if self.root == None:
            self.root = new_node

        else:
            current = self.root
            while(current.value is not None):
                if(current.left == None):
                    current.left = new_node
                    break
                current = current.left

    def check_if_BST(self):
        self.in_order_traversal(self.root)
        sorted_array = sorted(self.inorderarray)
        ctr = 0
        for i in range(len(sorted_array)):
            if(sorted_array[i] == self.inorderarray[i]):
                ctr += 1
        return ctr == len(self.inorderarray)

    def print_inorder(self):
        for i in self.inorderarray:
            print(i)

    def in_order_traversal(self,node):
        if(node is not None):
            self.in_order_traversal(node.left)
            self.inorderarray.append(node.value)
            self.in_order_traversal(node.right)

def main():
    my_BT = BinaryTree()
    my_BT.insert_to_right(5)
    my_BT.insert_to_left(4)
    my_BT.insert_to_right(8)
    print(my_BT.check_if_BST())
    my_BT.print_inorder()


if __name__ == '__main__':
    main()
