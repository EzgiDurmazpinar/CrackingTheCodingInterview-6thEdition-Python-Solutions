#4.9
#BST Sequences: A binary search tree was created by traversing through an array
#from left to right and inserting each element.
#Given a binary search tree with distinct elements,
#print all possible arrays that could have led to this tree.
class Node():
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.nodes = dict()
        self.preorder = []
        self.postorder = []
        self.inorder = []

    def add_nodes(self,arr):
        for i in arr:
            self.nodes[i] = Node(i)

        for element in arr:
            self.add(self.nodes[element])

    def add(self,new_node):

        if(self.root == None):
            self.root = new_node
        else:
            current = self.root
            while(current != None):
                if(new_node.value > current.value):
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

    def in_order(self,node):
        if(node!=None):
            self.in_order(node.left)
            self.inorder.append(node)
            self.in_order(node.right)

    def pre_order(self,node):
        if(node != None):
            self.preorder.append(node)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self,node):
        if(node != None):
            self.post_order(node.left)
            self.post_order(node.right)
            self.postorder.append(node)

    def print_all_possible(self):
        self.in_order(self.root)
        self.pre_order(self.root)
        self.post_order(self.root)

        print('inorder')
        for i in self.inorder:
            print(i.value,end= " ")
        print()
        print('preorder')
        for y in self.preorder:
            print(y.value,end= " ")
        print()
        print('postorder')
        for z in self.postorder:
            print(z.value,end= " ")
        print()
        #print('preorder')

def main():
    bst = BinarySearchTree()
    my_bst = [2,1,3]
    bst.add_nodes(my_bst)
    bst.print_all_possible()

if __name__ == '__main__':
    main()
