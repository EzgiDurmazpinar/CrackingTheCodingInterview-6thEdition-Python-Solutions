#PairwiseSwap: Write a program to swap odd and even bits in an integer with as few instructions as possible
#(e.g., bit 9 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
def swapOddandEven(number):
    #0xaaaaaaaa is = 10101010
    #0x55555555 is = 01010101
    print(bin(16))
    return ((number & 0xaaaaaaaa) >> 1) | ((number & 0x55555555) << 1)

def main():
    print(bin(swapOddandEven(16)))
if __name__ == '__main__':
    main()
