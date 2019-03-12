#3.3Stack of Plates: Imagine a (literal) stack of plates.
#If the stack gets too high, it might topple.
#Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
#Implement a data structure SetOfStacks that mimics this.
#SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
#SetOfStacks .push() and SetOfStacks .pop() should behave identically to a single stack
#(that is, pop( ) should return the same values as it would if there were just a single stack).
#FOLLOW UP
#Implement a function p o p A t ( i n t i n d e x ) which performsa pop operation on a specific sub-stack.
class Stack(object):

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.items:
			raise IndexError("Stack in empty")
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

	def is_empty(self):
		return not bool(self.items)

#..............SOLUTION ...........
class SetOfStacks(object):
    def __init__(self,capacity):
        self.stacks =[]
        self.capacity = capacity
        #I assumed stack numbers start with zero for my follow up solution

    def push(self,v):
        if len(self.stacks) != 0:
            last_stack = self.get_last_stack()
            if(last_stack.size() < self.capacity ):
                last_stack.push(v)
            else:
                new_stack = Stack()
                new_stack.push(v)
                self.stacks.append(new_stack)
        else:
            new_stack = Stack()
            new_stack.push(v)
            self.stacks.append(new_stack)

    def get_last_stack(self):
        if(len(self.stacks) !=0):
            return self.stacks[-1]

    def pop(self):
        if len(self.stacks) != 0:
            last_stack = self.get_last_stack()
            v = last_stack.pop()
            if(last_stack.size() == 0):
                self.stacks.pop()
            return v

    def print_all(self):
        for s in self.stacks:
            print(s.items)

#Follow Up

    def pop_at(self, stack_number):
        if (stack_number < 0) or (len(self.stacks) <= stack_number):
            return None

        if self.stacks[stack_number].size() == 0:
            return None

        return self.stacks[stack_number].pop()

def main():
    setofstacks = SetOfStacks(2)
    setofstacks.push(1)
    setofstacks.push(2)
    setofstacks.push(3)
    setofstacks.push(4)
    #setofstacks.pop()
    setofstacks.pop_at(0)
    setofstacks.print_all()


if __name__ == '__main__':
    main()
