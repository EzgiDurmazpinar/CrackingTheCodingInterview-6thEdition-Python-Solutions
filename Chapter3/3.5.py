#3.5
# Write a program to sort a stack such that the smallest items are on the top.
#You can use an additional temporary stack,
#but you may not copy the elements into any other data structure (such as an array).
#The stack supports the following operations: push, pop, peek, and is Empty.


#In my solution i assume that stack does not have a negative value or duplicate value
from Stack import Stack

def sort_stack(input_stack):
    sorted_stack = Stack() #Additional stack for sorting
    tmp_stack = Stack()

    for y in range(len(input_stack.my_stack)):
        biggest = -1
        for i in range(len(input_stack.my_stack)):
            if input_stack.my_stack[i] > biggest and input_stack.my_stack[i] not in tmp_stack.my_stack:
                biggest = input_stack.my_stack[i]
        tmp_stack.push(biggest)
        sorted_stack.push(biggest)

    for i in range(len(sorted_stack.my_stack)):
        print(sorted_stack.my_stack[i])

def main():
    mystack = Stack()
    mystack.push(1)
    mystack.push(5)
    mystack.push(3)
    mystack.push(2)
    mystack.push(8)

    sort_stack(mystack)

if __name__ == '__main__':
    main()
