#5.3
#Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1,
# Write code to find the length of the longest sequence of 1s you could create.

def flip_bit(binary_num):

    n = bin(binary_num)
    max_1_length = 1
    old_ctr = 0
    ctr = 0
    #print(len(n))
    #print(n)
    for i in range(2,len(n)+1): #Because binary nums in python like --> 0b11011101111
        if i<len(n) and n[i] == '1' :
            ctr+=1
        else:
            if old_ctr + ctr + 1 > max_1_length:
                max_1_length = old_ctr + ctr + 1
            
            old_ctr = ctr
            ctr = 0
    return max_1_length

def main():
    print(flip_bit(1775))

if __name__ == '__main__':
    main()
