#Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter- secting node.
#Note that the intersection is defined based on reference, not value.
#That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
from SinglyLinkedList import *

def intersection(ll1, ll2):
    #1.Run through each linked list to get the lengths and the tails.
    current1 = ll1.head
    current2 = ll2.head
    size1 = size2 = 0

#Get the size and tail of first linked list
    while(current1 != None):
        current1 = current1.next
        size1 += 1
    tail1 = current1

#Get the size and tail of second linked list
    while(current2 != None):
        current2 = current2.next
        size2 += 1
    tail2 = current2

    #Compare the tails. If they are different there is no Intersection
    if (tail1 != tail2) :
        return None


    #Set two pointers to the start of each linked list.
    current1 = ll1.head
    current2 = ll2.head

    #On the longer linked list, advance its pointer by the difference in lengths
    difference = abs(size1 - size2)
    ctr = 0
    if(size1>size2):
        while(ctr<difference):
            current1 = current1.next
            ctr += 1
    else:
        while(ctr<difference):
            current2 = current2.next
            ctr += 1

    #Move both pointers until have a collision
    while(current1 != current2):
        current1 = current1.next
        current2 = current2.next

    return current1

def main():

    mylist = SinglyLinkedList()
    intersected_node = Node(4)
    mylist.insert_node(1)
    mylist.insert_node(2)


    mylist2 = SinglyLinkedList()
    mylist2.insert_node(4)
    mylist2.insert_node(2)

    print(intersection(mylist,mylist2))

if __name__ == '__main__':
    main()
