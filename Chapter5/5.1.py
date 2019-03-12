#5.1
#Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and j.
#Write a method to insert M into N such that M starts at bit j and ends at bit i.
#You can assume that the bits j through i have enough space to fit all of M. That is, if M = 10011,
# you can assume that there are at least 5 bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.

def Insertion(N,M,i,j):

    if i>j or i<0 or j>=32:
        return False

    #First of all I need to clear bits through i to j to insert M into N
    mask1 = 1<<i
    mask2 = 1<<j+1
    mask = (mask2 - mask1)
    N_cleared = N & ~(mask)
    M_shifted = M << i

    return N_cleared | M_shifted

def main():

    N = 0b10000000000
    M = 0b10011
    i =2
    j = 6
    print(Insertion(N,M,i,j))

if __name__ == "__main__":
    main()
