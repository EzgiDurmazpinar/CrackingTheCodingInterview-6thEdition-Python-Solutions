#5.4
#Next Number: Given a positive integer,
#print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.
def get_next(number):
    #compute c0 and c1
    c = n
    c0 = 0
    c1 = 0
    while(c&1) ==0 and c!=0:
        c0+=1
        c>>=1

    while(c&1 ==1):
        c1+=1
        c>>=1

    if(c0 + c1 == 31 or c0+c1 == 0 ):
        return

    p = co+c1
    n |= 1<<p
    n &= ~((1<<p) - 1)
    n |= (1<<(c1 - 1)) - 1
    return n

def get_previous()
    pass
    
