#4.6
#Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.
#You may assume that each node has a link to its parent.

class Node():

    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

class BST():

    def __init__(self):
        self.root = None


    def insert_node(self,node):

        if(self.root == None):
            self.root = node
        else:
            current = self.root
            while(current != None):
                if node.value < current.value:
                    if(current.left == None):
                        current.left = node
                        node.parent = current
                        break
                    else:
                        current = current.left
                else:
                    if(current.right == None):
                        current.right = node
                        node.parent = current
                        break
                    else:
                        curent = current.right

    def find_next_successor(self,node):
        visited = []
        curr = self.root
        while curr != None:         #Mark visited ones from right subtree
            if(node.value < curr.value):
                curr = curr.left
            elif node.value > curr.value:
                visited.append(curr)
                curr = curr.right
            else:
                break

        current = node
        if node.right != None:      #case1: If node has a subtree : go deep to leftmost node in right subtree
            current = current.right
            while(current.left != None):
                current = current.left
            return current.value
        else:                       #case2 :If node has no right subtree : go to the nearest ancestor that is not visited before
            if current.parent in visited:
                return current.parent.parent.value
            else:
                return current.parent.value


def main():
    my_bst = BST()
    node1 = Node(7)
    node2 = Node(5)
    node3 = Node(4)
    node4 = Node(6)
    node5 = Node(8)
    my_bst.insert_node(node1)
    my_bst.insert_node(node2)
    my_bst.insert_node(node3)
    my_bst.insert_node(node4)
    my_bst.insert_node(node5)
    print(my_bst.find_next_successor(node1))

if __name__ == '__main__':
    main()
