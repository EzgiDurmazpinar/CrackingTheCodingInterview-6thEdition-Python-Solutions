#Check Balanced: Implement a function to check if a binary tree is balanced.
#For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.


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

    def check_if_balanced(self):
        current = self.root
        ctrL = 0
        while(current != None):
            current = current.left
            ctrL+=1
        current = self.root
        ctrR = 0
        while(current != None):
            current = current.right
            ctrR+=1

        print('Left side is {}'.format(ctrL-1))
        print('Right side is {}'.format(ctrR-1))
        if abs(ctrL - ctrR) <= 1:
            return True
        else:
            return False

def main():
    mytree = BinarySearchTree()
    mytree.add(5)
    mytree.add(3)
    mytree.add(8)
    mytree.add(12)
    mytree.add(2)
    mytree.add(1)
    

    print(mytree.check_if_balanced())

if __name__ == '__main__':
    main()
