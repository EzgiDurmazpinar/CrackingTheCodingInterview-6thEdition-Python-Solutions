#5.6.py
#Conversion: Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
#EXAMPLE
#Input: 29 (or: 11101), 15 (or: 01111) Output: 2

def conversion(num1,num2):
    c = num1 ^ num2
    count = 0
    while(c!=0):
        count += c&1
        c>>=1
    return count

def main():
    print(conversion(29,15))

if __name__ == '__main__':
    main()
