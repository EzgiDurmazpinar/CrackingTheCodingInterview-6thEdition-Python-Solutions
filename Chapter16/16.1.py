#16.1
#Number Swapper: Write a function to swap a number in place (that is, without temporary variables).

def number_swapper(a,b):
    print('a is {}'.format(a))
    print('b is {}'.format(b))

    if a>b:
        a = a-b
        b = b+a
        a = b-a
    elif b>a:
        b = b - a
        a = a + b
        b = a-b
    else: #they are already equal
        a=b
        b=a

    print('a is {}'.format(a))
    print('b is {}'.format(b))

def main():
    number_swapper(3,8)

if __name__ == '__main__':
    main()
