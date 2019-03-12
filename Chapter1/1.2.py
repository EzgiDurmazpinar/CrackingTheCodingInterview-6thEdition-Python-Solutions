#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other

#I use sorted() built in funtion to first sort arrays
#It’s called Timsort. It's an exceptionally adaptive merge sort, which is miraculous in practice, but asymptotically it’s no better than merge sort: 𝑂(𝑛log𝑛).
class myString():
    def __init__(self,string):
        self.s = list()
        self.s = string
        self.s = sorted(self.s)


    def isPermutationOfOther(self,string):
        string2 = list()
        string2 = string

        if(len(self.s) == len(string2)):
            string2 = sorted(string2)


            for i in range(len(self.s)):
                if self.s[i].lower() == string2[i].lower():
                    continue
                else:
                    print('They are not permutation of each other')
                    return True
            print('They are permutation of each other')
            return False
        else:
            print('They are not permutation of each other')
            return False

def main():
    StringEzgi  = myString('Ahmet')
    StringEzgi.isPermutationOfOther('igzek')

if __name__ == '__main__':
    main()
