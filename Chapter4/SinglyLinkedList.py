#IMPLEMENT A LINKED LIST IN PYTHON
class Node():
    def __init__(self,value = None ):
        self.value = value
        self.next = None
    def set_next(self,next_value): #dont need it but in case
        self.next = next_value


class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def print_linkedlist(self):
        printing_value = self.head
        while(printing_value is not None):
            print(printing_value.value)
            printing_value = printing_value.next

    def insert_node(self,node_value):
        new_node = Node(node_value)

        if (self.head == None):
            self.head = new_node
        else:
            node = self.head
            while(node.next is not None):
                node = node.next
            node.next = new_node

    def insert_beginning(self,node_value):
        new_node = Node(node_value)
        new_node.next = self.head
        self.head = new_node

    def get_size(self):
        value = self.head
        ctr = 0
        while(value is not None):
            value = value.next
            ctr+=1
        return ctr

    def delete_node(self,node_value):
        node = self.head
        prev_node = node
        found = False
        while(node.next is not None):
            if(self.head.value == node_value):
                self.head = self.head.next
                found = True
                break
            elif node.value == node_value:
                prev_node.set_next(node.next)
                found = True
                break
            else:
                prev_node = node
                node = node.next

        if found == False:          #If you are trying to delete the latest one in linked list
            if node.value == node_value:
                prev_node.set_next(None)


def main():


    mylist = SinglyLinkedList()

    mylist.insert_node(1)
    mylist.insert_node(2)
    mylist.insert_node(3)
    mylist.insert_node(4)

    mylist.delete_node(1)
    mylist.delete_node(4)

    mylist.print_linkedlist()

if __name__ == '__main__':
    main()
