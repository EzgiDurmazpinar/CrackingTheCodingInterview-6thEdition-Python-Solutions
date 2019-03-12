#2.2
#Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

#This part is just the implementation of Linked list not solution to this problem
class Node():
    def __init__(self,value = None ):
        self.value = value
        self.next = None
    def set_next(self,next_value):
        self.next = next_value


class SinglyLinkedList():
    def __init__(self):
        self.headValue = None

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
#-------------------------------------------------------------------------------
#SOLUTION TO THIS PROBLEM
def kth_to_last(linkedlist,k):

    current = linkedlist.headValue
    ctr = 1
    while(ctr<k and current.next != None):
        current = current.next
        ctr+=1

    while(current.next != None):
        print(current.value)
        current = current.next

    print(current.value)
#---------SOLUTION ENDS HER----------------------

#Driver code
def main():
    linkedlist = SinglyLinkedList()
    linkedlist.insert_node(1)
    linkedlist.insert_node(2)
    linkedlist.insert_node(3)
    linkedlist.insert_node(5)

    kth_to_last(linkedlist,3)

if __name__ == '__main__':
    main()
