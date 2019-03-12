#List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
#(e.g., if you have a tree with depth 0, you'll have 0 linked lists).
from SinglyLinkedList import SinglyLinkedList

class Node():
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value
        self.lists = []

class BinaryTree():
    def __init__(self):
        self.binary_tree = []
        self.root = None

    def add(self,value):
        new_node = Node(value)
        if(len(self.binary_tree) == 0):
            self.binary_tree.append(new_node)
            self.root = new_node
        else:
            current = self.root
            while(current != None):
                if(value > current.value):
                    if(current.right == None):
                        current.right = new_node
                        break
                    else:
                        current = current.right
                else:
                    if(current.left == None):
                        current.left = new_node
                        break
                    else:
                        current = current.left


    def make_it_array(self,node):
        if(node != None):
            self.binary_tree.append(node.value)
            self.make_it_array(node.left)
            self.make_it_array(node.right)


    def print_my_tree(self):
        for i in range(len(self.binary_tree)):
            print(self.binary_tree[i])

    def create_level_ll(self,root):
        result = [] #lis of linkedlists
        current = SinglyLinkedList()
        if(root != None):
            current.insert_node(root)
        while(current.get_size()>0):
            result.append(current)
            parents = SinglyLinkedList()
            parents = current
            current = SinglyLinkedList()
            parent = parents.head
            while(parent is not None):
                if parent.left != None:
                    current.insert_node(parent.left)
                if parent.right != None:
                    current.insert_node(parent.right)
                parent = parent.next
        return result



def main():
    my_binary_tree = BinaryTree()

    my_binary_tree.add(1)
    my_binary_tree.add(3)
    my_binary_tree.add(0)
    my_binary_tree.add(6)
    my_binary_tree.add(4)

    #my_binary_tree.make_it_array(my_binary_tree.root)
    #my_binary_tree.print_my_tree()
    my_binary_tree.create_level_ll(my_binary_tree.root)
if __name__ == '__main__':
    main()
