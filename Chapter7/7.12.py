#Hash Table: Design and implement a hash table which uses chaining (linked lists) to handle collisions.
class Node():
    def __init__(self,value):
        self.next = None
        self.value = value

class LinkedList():
    def __init__(self):
        self.root = None

    def add(self,node):
        if self.root == None:
            self.root = node
        else:
            curr = self.root
            while(curr.next != None):
                curr = curr.next
            curr.next = node

    def delete(self,value):
        found = False
        if self.root == None:
            return None
        else:
            curr = self.root
            while(curr.next != None):
                if(curr.value == value):
                    if curr == self.root:
                        self.root = curr.next
                    else:
                        prev.next = curr.next
                    found =True
                prev = curr
                curr = curr.next

            if found == False:
                prev.next = None

class HashTable():
    def __init__(self,size):
        self.hash_table = {}
        self.array = [None for i in range(size)]
        self.count = 0
        self.capacity = 0.75 * size
        self.lls = {}

    def add_method(self,value):
        if(self.capacity > self.count +1):
            self.count +=1
            self.hash_table[self.count] = Node(value)
        else:                           #If it is a collision
            self.count +=1
            idx = self.count % self.capacity
            if idx in self.hash_table:
                ll = LinkedList()
                ll.add(self.hash_table[idx])
                node = Node(value)
                ll.add(node)
                self.hash_table[idx] = ll
            else:
                self.hash_table[idx] = Node(value)

    def print_mytable(self):
        for key,value in self.hash_table.items():
            print(value)


def main():
    myhashtable = HashTable(5)
    myhashtable.add_method(1)
    myhashtable.add_method(2)
    myhashtable.add_method(3)
    myhashtable.add_method(4)
    myhashtable.print_mytable()
if __name__ == '__main__':
    main()
