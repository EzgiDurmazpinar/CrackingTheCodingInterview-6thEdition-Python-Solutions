class Queue():  #First In First out

    def __init__(self):
        self.my_queue = list()

    def add(self,item):
        self.my_queue.append(item)

    def remove(self):
        removed =self.my_queue[0]
        self.my_queue.pop(0)
        return removed

    def peek(self):     #Return the top of stack
        if(self.my_queue[0] != None):
            return self.my_queue[0]

    def isEmpty(self):
        return len(self.my_queue) == 0
