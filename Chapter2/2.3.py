#Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
#EXAMPLE
#Input: the node c from the linked list a - >b- >c - >d - >e- >f
#Result: nothing is returned, but the new linked list looks like a->b->d->e->f Hints: #72
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


#SOLUTION
def delete_node(linkedlist):
    current = linkedlist.headValue
    if current.next == None or current == None or current.next.next == None:
        return False
    else:
        current = current.next
        current.value = current.next.value
        current.next = current.next.next
        return True

def main():
    mylist = SinglyLinkedList()

    mylist.insert_node(1)
    mylist.insert_node(2)


    print(delete_node(mylist))
    mylist.print_linkedlist()
if __name__ == '__main__':
    main()
