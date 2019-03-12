from SinglyLinkedList import SinglyLinkedList
#Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
#The digits are stored in reverse order, such that the 1's digit is at the head of the list.
#Write a function that adds the two numbers and returns the sum as a linked list.
#EXAMPLE
#Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. Output: 2 -> 1 -> 9. That is, 912.

def sum_lists(ll1, ll2):
    new_ll = SinglyLinkedList()
    current1 = ll1.head
    current2 = ll2.head
    carry, result = 0, 0
    while(current1 != None and current2 != None):
        res = carry
        res += current1.value + current2.value
        carry = (res - (res%10)) // 10
        res  = res%10
        new_ll.insert_node(res)
        current1 = current1.next
        current2 = current2.next

    new_ll.print_linkedlist()

#FOLLOW UP
#Suppose the digits are stored in forward order. Repeat the above problem.
#EXAMPLE Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295, Output:9 -> 1 -> 2,Thatis,912.
def sum_lists_followup(ll1, ll2):
    s1, s2 = ll1.get_size() , ll2.get_size()
    current1 = ll1.head
    current2 = ll2.head
    new_list = SinglyLinkedList()
    if(s1 != s2):
        #If their size is not equal first pad zeros to the shorter one
        if(s1> s2):
            for i in range(s1 - s2):
                ll2.insert_beginning(0)
        else:
            for i in range(s1 - s2):
                ll1.insert_beginning(0)
    else:

        result = 0
        while(current1 != None and current2 != None):
            result = (result * 10) + current1.value + current2.value
            current1 = current1.next
            current2 = current2.next
        for i in str(result):
            new_list.insert_node(int(i))

        new_list.print_linkedlist()

def main():

    mylist = SinglyLinkedList()
    mylist.insert_node(7)
    mylist.insert_node(1)
    mylist.insert_node(6)

    mylist2 = SinglyLinkedList()
    mylist2.insert_node(5)
    mylist2.insert_node(9)
    mylist2.insert_node(2)

    #sum_lists(mylist, mylist2)
    sum_lists_followup(mylist,mylist2)
if __name__ == '__main__':
    main()
