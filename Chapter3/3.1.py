#Three in One: Describe how you could use a single array to implement three stacks.
#In my solution I've assumed that user will not oush values more than fixed stack sizes
from Stack import Stack

class ThreeStackAtOne():
    def __init__(self,stacksize):
        self.stack_size = stacksize
        self.my_stack = [0] *(stacksize*3)
        self.stackNumbers = [0,1,2]

    def pop(self,stackNum):   #Remove the top item from Stack
        if stackNum in self.stackNumbers:
            poped_value = self.my_stack[stackNum*(self.stack_size)]
            self.my_stack = self.my_stack[stackNum*(self.stack_size)+1:]
            return poped_value
        else:
            print("Wrong Stack Number")

    def push(self,item,stackNum):    #Push item to the top
        if stackNum in self.stackNumbers:
            self.my_stack[stackNum*(self.stack_size):0] = [item]
        else:
            print("Wrong Stack Number")

    def peek(self,stackNum):     #Return the top of stack

        if stackNum in self.stackNumbers:
            return self.my_stack[stackNum*(self.stack_size)]

        else:
            print("Wrong Stack Number")

    def isEmpty(self,stackNum):

        if stackNum in self.stackNumbers:
            top = stackNum*(self.stack_size)
            ctr = 0
            for i in range(len(self.stack_size)):
                if self.my_stack[top+i] == None:
                    ctr +=1
            return ctr == self.stack_size

        else:
            print("Wrong Stack Number")

def main():
    my_stacks_in_one = ThreeStackAtOne(2)
    my_stacks_in_one.push(5,0)
    my_stacks_in_one.push(4,0)
    my_stacks_in_one.push(6,1)
    my_stacks_in_one.push(7,2)
    print(my_stacks_in_one.pop(0))
    print(my_stacks_in_one.my_stack)

if __name__ == "__main__":
    main()
