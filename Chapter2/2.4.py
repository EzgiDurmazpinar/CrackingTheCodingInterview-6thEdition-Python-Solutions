#Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. Ifxis contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
#EXAMPLE
#Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
#Hints: #3, #24
class Node():
    def __init__(self,value = None ):
        self.value = value
        self.next = None
    def set_next(self,next_value):
        self.next = next_value


class SinglyLinkedList():
    def __init__(self):
        self.headValue = None
        self.tailValue = None
    def print_linkedlist(self):
        printing_value = self.headValue
        while(printing_value is not None):
            print(printing_value.value)
            printing_value = printing_value.next

    def insert_node(self,node_value):
        new_node = Node(node_value)

        if (self.headValue == None):
            self.headValue = new_node
        else:
            node = self.headValue
            while(node.next is not None):
                node = node.next
            node.next = new_node
 #SOLUTION
def partition_linkedlist(linkedlist,x):
    current = linkedlist.headValue
    newList = SinglyLinkedList()
    tail_node = head_node = current

    while(current != None):
        nextNode = current.next
        current.next = None
        if current.value < x:
            #Insert node at the head
            current.next = head_node
            head_node = current
        else:
            #Insert node at the tail
            tail_node.next = current
            tail_node = current
        current = nextNode
    tail_node.next = None

    newList.headValue = head_node
    newList.print_linkedlist()

def main():
    mylist = SinglyLinkedList()
    mylist.insert_node(3)
    mylist.insert_node(5)
    mylist.insert_node(8)
    mylist.insert_node(5)
    mylist.insert_node(10)
    mylist.insert_node(2)
    mylist.insert_node(1)
    partition_linkedlist(mylist,5)


if __name__ == '__main__':
    main()
