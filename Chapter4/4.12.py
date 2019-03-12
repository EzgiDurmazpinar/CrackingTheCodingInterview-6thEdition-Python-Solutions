#Paths with Sum: You are given a binary tree in which each node contains an integer value
#(which might be positive or negative).
#Design an algorithm to count the number of paths that sum to a given value.
#The path does not need to start or end at the root or a leaf,
#but it must go downwards (traveling only from parent nodes to child nodes).
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

    def sum_of_path(self,sum,curr):
        sum_of_path= []
        total_sum = curr.value
        sum_of_path.append(curr.value)

        while(curr != None and total_sum != sum):
            if(curr.right != None):
                total_sum += curr.right.value
                sum_of_path.append(curr.right.value)
                curr = curr.right
            elif curr.left != None:
                total_sum += curr.left.value
                sum_of_path.append(curr.left.value)
                curr = curr.left
            else:
                if(total_sum == sum):
                    return  sum_of_path
                else:

                    return False

        if(total_sum == sum):
            return  sum_of_path
        else:
            return False

    def  find_sum_path(self,sum):
        curr = self.root
        list_of_paths = []
        while(curr!=None):
            if(curr.left !=None):
                list_of_paths.append(self.sum_of_path(sum,curr.left))
                curr = curr.left
            if(curr.right !=None):
                print('burdssn gceti')
                list_of_paths.append(self.sum_of_path(sum,curr.right))
                curr = curr.right
            break


        return list_of_paths

def main():
    bt = BinaryTree()
    bt.insert_to_left(4)
    bt.insert_to_left(3)
    bt.insert_to_left(2)
    bt.insert_to_right(5)

    print(bt.find_sum_path(9))


if __name__ == '__main__':
    main()
