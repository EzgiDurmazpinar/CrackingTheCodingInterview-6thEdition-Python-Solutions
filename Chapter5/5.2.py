#5.2
#Binary To String
#Given a real number between 0 and 1 (eg., 0.72) that is passed in as double,
#print the binary representation.If the number cannot be represented accurately in binary with most 32 characters, print ERROR

def Binary_to_string(num):
    if num >= 1 or num<0:
        return "ERROR"
    converted = "."

    while(num < 1):
        num *= 2
        if(num < 1):
            converted +='0'
        else:
            converted +='1'
    return converted

def main():
    num = 0.125
    print(Binary_to_string(0.125))

if __name__ == '__main__':
    main()
