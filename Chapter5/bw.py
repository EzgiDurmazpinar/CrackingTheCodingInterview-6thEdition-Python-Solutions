#SOME FUNCTIONS THAT NEEDED TO BE KNOWIN BITWISE OPERATION
#Get Bit


#This method shifts 1 over by i bits, creating a value like 00010000
#by performing an and with num we clear all the bits than bit i .
#then compare it with zero . if it is not zero then bit must be 1 otherwise it is zero.
def get_bit(num,i):
    return (num & (1 << i)) != 0
#by performing an OR with num only the i'th bit will change.
def set_bit(num,i):
    return (num | (1 << i))

def clear_bit(num,i):
    return (num & ~(1 << i))
