#CheckPrime

def isprime(x):

    if(x<2):
        return False
    else:

        for i in range(2, x-1):
            if x % i == 0:
                return False

        return True


def main():

    print(isprime(15))
    print(isprime(11))
    
if __name__ == '__main__':
    main()
