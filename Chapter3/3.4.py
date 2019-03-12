#3.4
#Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
from Stack import Stack

class Myqueue(object):

    def __init__(self):
        self.newest_stack = Stack()
        self.oldest_stack = Stack()

    def size(self):
        return (self.newest_stack.size() + self.oldest_stack.size())

    def add(self,val):
        self.newest_stack.push(val)

    def shift_stacks(self):
        if self.oldest_stack.isEmpty():
            while(not self.newest_stack.isEmpty()):
                self.oldest_stack.push(self.newest_stack.pop())

    def peek(self):
        self.shift_stacks()
        return self.oldest_stack[len(self.oldest_stack) - 1]

    def remove(self):
        self.shift_stacks()
        self.oldest_stack.pop()

    def print_my_queue(self):
        self.shift_stacks()
        self.oldest_stack.print_stack()


def main():
    q = Myqueue()
    q.add(1)
    q.add(4)
    q.add(5)
    q.remove()
    q.print_my_queue()
    print()
if __name__ == '__main__':
    main()
