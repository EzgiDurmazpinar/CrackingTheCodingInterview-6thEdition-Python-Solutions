#Random Node: You are implementing a binary tree class from scratch which, in addition to insert, find, and delete,
#has a method getRandomNode() which returns a random node from the tree.
#all nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode,
#and explain how you would implement the rest of the methods.
import random
class Node():

    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None


class BST():

    def __init__(self):
        self.root = None
        self.nodes = {}
        self.values = []

    def insert_node(self,value):
        node = Node(value)
        self.nodes[value] = node
        self.values.append(value)

        if(self.root == None):
            self.root = node
        else:
            current = self.root
            while(current != None):

                if node.value < current.value:
                    if(current.left == None):
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if(current.right == None):
                        current.right = node
                        break
                    else:
                        current = current.right

    def get_random_node(self):
        randInt = random.randint(0,len(self.values)-1)
        return self.nodes[self.values[randInt]]

def main():
    my_bst = BST()
    my_bst.insert_node(5)
    my_bst.insert_node(4)
    my_bst.insert_node(3)
    my_bst.insert_node(8)
    my_bst.insert_node(6)

    node = my_bst.get_random_node()
    print(node.value)

if __name__ == '__main__':
    main()
