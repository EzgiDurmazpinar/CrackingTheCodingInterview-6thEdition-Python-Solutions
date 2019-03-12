#Stack Min: How would you design a stack which, in addition to push and pop,
#has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class Stack():
    #ASLINDA SONUNDAN EKLEYIP SONUNDAN CIKARIYOR AMA son giren ilk cikiyor son tarafi top gibi dusun
    def __init__(self):
        self.my_stack = list()
        self.min = self.prev_min = 100


    def pop(self):   #Remove the top item from Stack
        if self.isEmpty() == False:
            if self.peek() == self.min:
                self.min = self.prev_min
            self.my_stack.pop()
        else:
            print('Stack is Empty')

    def push(self,item):    #Push item to the top
        if self.isEmpty() == False:
            if item < self.min :

                self.prev_min = self.min
                self.min = item
        else:
            self.min = item

        self.my_stack.append(item)


    def peek(self):     #Return the top of stack
        if(self.isEmpty()):
            raise Exception('Stack is empty!')
        else:
            return self.my_stack[len(self.my_stack)-1]

    def isEmpty(self):
        return len(self.my_stack ) == 0

    def my_min(self):
        print('Min is {}'.format(self.min))

    def my_stack_size(self):
        return len(self.my_stack)

def main():
    mystack = Stack()
    mystack.push(1)
    mystack.push(4)
    mystack.push(0)
    print(mystack.my_stack)
    mystack.my_min()
    mystack.pop()

    print(mystack.my_stack)
    mystack.my_min()
    #print(mystack.peek())





if __name__ == "__main__":
    main()
