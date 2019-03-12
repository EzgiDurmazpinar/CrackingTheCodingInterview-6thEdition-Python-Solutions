#8.9
#Parens: implement an algorithm to print all valid (e.g., properly opened and closed)
#combinations of n pairs of parentheses.
def add_parens(list, leftRem, rightRem, str):

    if(leftRem <0 or rightRem <leftRem):
         return
    if (leftRem == 0 and rightRem ==0):
        list.append(str)
    else:
        str.append('(')
        add_parens(list,leftRem-1,rightRem,str)

        str.append(')')
        add_parens(list,leftRem,rightRem-1,str)

def generate_parens(count):
    str = []
    l = list()
    add_parens(l,count,count,str)
    return l

def main():
    print(generate_parens(3))

if __name__ == '__main__':
    main()
