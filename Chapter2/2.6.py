#Palindrome: Implement a function to check if a linked list is a palindrome.
#Hints: #5, #13, #29, #61, #101
from SinglyLinkedList import SinglyLinkedList
def isPalindrome(linkedlist):
    current = linkedlist.head
    d = dict()

    while(current != None):
        if current.value in d:
            d[current.value] += 1
        else:
            d[current.value] = 1
        current = current.next

    odd_ctr = 0
    even_ctr = 0

    for key,value in d.items():
        if value%2 == 0:
            even_ctr+=1
        else:
            odd_ctr +=1

    if(odd_ctr>1):
        return False
    else:
        return True

def main():

    mylist = SinglyLinkedList()
    mylist.insert_node(1)
    mylist.insert_node(2)
    mylist.insert_node(3)
    mylist.insert_node(4)
    mylist.insert_node(2)
    mylist.insert_node(1)

    print(isPalindrome(mylist))

if __name__ == '__main__':
    main()
