#Implementataion of Stack python    Last In First Out push from top and pop from top
#List is a dynamic array in pyhton

class Stack():
    #ASLINDA SONUNDAN EKLEYIP SONUNDAN CIKARIYOR AMA son giren ilk cikiyor som tarafi top gibi dusun
    def __init__(self):
        self.my_stack = list()

    def pop(self):   #Remove the top item from Stack
        return self.my_stack.pop()

    def push(self,item):    #Push item to the top
        self.my_stack.append(item)

    def peek(self):     #Return the top of stack
        return self.my_stack[len(list)-1]

    def isEmpty(self):
        return len(self.my_stack ) == 0

    def size(self):
        return len(self.my_stack)

    def print_stack(self):
        for i in range(len(self.my_stack)):
            print(self.my_stack[i])
