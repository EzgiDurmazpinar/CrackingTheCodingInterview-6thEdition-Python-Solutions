#4.10
#Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
#algorithm to determine if T2 is a subtree o f T1

class Node():
    def __init__(self,value):
        self.right = 'X'
        self.left = 'X'
        self.value = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.preorder = []

    def insert_to_right(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node

        else:
            current = self.root
            while(current.value is not None):
                if(current.right == 'X'):
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
                if(current.left == 'X'):
                    current.left = new_node
                    break
                current = current.left
    def pre_order(self,node):
        if(node != 'X' and node!=None):
            self.preorder.append(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

def contains_tree(t1,t2):
    if (t2.root == None):
        return True
    elif (t1.root == None):
        return False
    else:
        t1.pre_order(t1.root)
        t2.pre_order(t2.root)
    ctr = 0

    for y in range(len(t1.preorder)): #T1 is the big tree
        if t2.preorder[0] == t1.preorder[y]:
            idx = y
            for i in range(len(t2.preorder)):
                if(t2.preorder[i] == t1.preorder[idx]):
                    ctr +=1
                    idx +=1
                    break
        print
        return ctr == len(t2.preorder)
def main():
    my_BT = BinaryTree()
    my_BT.insert_to_right(5)
    my_BT.insert_to_left(4)
    my_BT.insert_to_right(8)
    my_BT.insert_to_left(9)

    my_BT2 = BinaryTree()
    my_BT2.insert_to_right(5)
    my_BT2.insert_to_left(4)
    my_BT2.insert_to_right(8)

    print(contains_tree(my_BT,my_BT2))

if __name__ == '__main__':
    main()
