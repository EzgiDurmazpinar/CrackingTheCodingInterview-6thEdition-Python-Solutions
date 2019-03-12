#This program finds least common ancestor of two nodes in a binary search tree
class Node():
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value


class BinarySearchTree():
    def __init__(self):
        self.binary_tree = []
        self.root = None

    def add(self,value):
        new_node = Node(value)
        if(self.root == None):
            self.root = new_node
            #print(self.root.value)
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
    def find_LCA(self,node1,node2):
        root = self.root
        while(root != None):
            #If both n1 and n2 smaller than root, then LCA lies in left
            if (node1<root.value and node2<root.value):
                root = root.left
            #If both n1 and n2 greater than root , then LCA lies in right
            elif (node1>root.value and node2>root.value):
                root = root.right
            else:
                break
        return root.value

def main():
    my_bst = BinarySearchTree()
    my_bst.add(6)
    my_bst.add(4)
    my_bst.add(9)
    my_bst.add(18)
    my_bst.add(8)
    my_bst.add(5)
    my_bst.add(3)

    print(my_bst.find_LCA(3,9))

if __name__ == '__main__':
    main()
