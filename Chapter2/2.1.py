#2.1 (LINKED LIST CHAPTER)
#Remove Dups: Write code to remove duplicates from an unsorted linked list. FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed? Hints: #9, #40

#Linkedlist Implementation
#-----------------------------------------------------------------------------
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

    def delete_node(self,node_value):
        node = self.headValue
        prev_node = node
        found = False
        while(node.next is not None):
            if(self.headValue.value == node_value):
                self.headValue = self.headValue.next
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
#-----------------------------------------------------------------------------
#Solution to 2.1
#Remove duplicates with temporary buffer
def remove_duplicates(linkedlist):

    d = dict()
    node = linkedlist.headValue
    while(node.next is not None):

        if node.value in d:
            linkedlist.delete_node(node.value)
        else:
            d[node.value] = 1

        node = node.next

    if node.value in d:                 #For the last element
        linkedlist.delete_node(node.value)

#Remove duplicates without temporary buffer solution
def delete_dups(linkedlist):

#If we don't have a buffer, we can iterate with two pointers:
#current which iterates through the linked list, and runner which checks all subsequent nodes for duplicates.

    current = linkedlist.headValue
    while(current is not None):
        #Remove all future nodes that have the same value
        runner = current
        while(runner.next is not None):
            if(runner.next.value == current.value):
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


def main():

    mylist = SinglyLinkedList()
    mylist.insert_node(2)
    mylist.insert_node(2)
    mylist.insert_node(2)
    mylist.insert_node(1)

    #remove_duplicates(mylist)
    delete_dups(mylist)
    mylist.print_linkedlist()


if __name__ == '__main__':
    main()
