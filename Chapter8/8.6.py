#8.6
#Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
#(1) Only one disk can be moved at a time.
#(2) A disk is slid off the top of one tower onto another tower.
#(3) A disk cannot be placed on top of a smaller disk.
#Write a program to move the disks from the first tower to the last using stacks.
#pseudocode
'''
def move_disks(n,tower_origin,tower_destination,tower_buffer):
    if (n<=0):
        return 0
    #Move top n-1 disks from origin to buffer , using destination as tower_buffer
    move_disks(n-1,tower_origin,tower_buffer,tower_destination)

    #Move top from origin to tower_destination
    move_top(origin,destination)

    #Move top n-1 disks from buffer to destination, using origin as tower_buffer
    move_disks(n-1,buffer,tower_destination,tower_origin)

'''

class Tower(): #implementing tower as a stack approach
    def __init__(self):
        self.disks = []

    def add_disc(self,n):
        self.disks.append(n)

    def move_top_to(self,other):
        disc = self.disks.pop()
        other.disks.append(disc)

    def move_disks(n,self,tower_destination,tower_buffer):
        if n <= 0:
            return 0
        self.move_disks(n-1,self,tower_buffer,tower_destination)
        self.move_top_to(destination)
        self.move_disks(n-1,tower_buffer,tower_destination,self)
