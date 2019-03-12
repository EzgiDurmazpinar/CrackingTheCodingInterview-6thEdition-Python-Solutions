#8.5 Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator.
#You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

def recursive_multiply(a,b):
    if a<b:
        return recursive_multiply(b,a)
    if b==0:
        return 0
    return a + recursive_multiply(a,b-1)

def main():
    print(recursive_multiply(3,2))
if __name__ == '__main__':
    main()
