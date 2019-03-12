#Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
#DEFINITION
#Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
#EXAMPLE
#Input: A -> B -> C -> D -> E -> C[the same C as earlier) Output: C
from SinglyLinkedList import *
def detectLoop(ll):
    slow_ptr = fast_ptr = ll1.head #Create two pointers, FastPointer and SlowPointer.


    while(fast_ptr != None and fast_ptr.next != None):
        slow_ptr = slow_ptr.next            #2. Move Fast Pointer at a rate of 2 steps and Slow Pointer at a rate of 1 step.
        fast_ptr = fast_ptr.next.next
        if(slow_ptr == fast_ptr):
            break

    if fast_ptr == None or fast_ptr.next == None: 3It means ll dont have a loop
        return None

    slow_ptr = head #3. When they collide, move SlowPointer to LinkedListHead.

    while(slow_ptr != fast_ptr): #4. Keep FastPointer where it is. 4. Move SlowPointer and FastPointer at a·rate of one step. Return the new collision point.
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    return fast_ptr #both of them points to the beginning of the loop now
