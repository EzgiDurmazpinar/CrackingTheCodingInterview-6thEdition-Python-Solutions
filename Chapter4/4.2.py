#Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
#write an algorithm to create a binary search tree with minimal height.

class Node():
    def __init__(self,item):
        self.right = None
        self.left = None
        self.value = item
    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.value) + " R:" + str(self.right)+')'

def create_minimal_BST(arr,start,end):
    if (end<start):
        return None
    mid = (start + end) // 2
    new_node = Node(arr[mid])
    new_node.left = create_minimal_BST(arr,start,mid-1)
    new_node.right = create_minimal_BST(arr,mid+1,end)
    return new_node

def main():
    arr = [1,2,3,4,5]
    print(create_minimal_BST(arr,0,len(arr)-1))

if __name__ =='__main__':
    main()
