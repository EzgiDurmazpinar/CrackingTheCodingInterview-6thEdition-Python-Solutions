#URLify: Write a method to replace all spaces in a string eith '%20'.
#You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string
class MyString():
    def __init__(self,s):
        self.String = s

    def replace(self):
        #self.String = "%20".join(self.String.split(" "))
        self.String = self.String.replace(" ", "%20")
        print(self.String)
def main():
    String1 = MyString('Mr 3ohn Smith')
    String1.replace()

if __name__ == '__main__':
    main()
