#Is Unique
#1.1
#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structure?

#With data structures:
'''
class Mystring():
    def __init__(self,string):
        self.StringList = list()
        self.StringList = string
    def isUnique(self):
        sizeBefore = len(self.StringList)
        sizeAfter = len(set(self.StringList))
        if (sizeBefore == sizeAfter):
            print('Yes it is.')
        else:
            print('No it is not.')

def main():
    firstString = Mystring('uniqse')  #which not all characters are uniqie
    firstString.isUnique()

if __name__ == "__main__":
    # execute only if run as a script
    main()
'''
#Without any data structures
class Mystring():
    def __init__(self,string):
        self.mystring = []
        self.mystring = string
#Better version is:
    def isUnique(self):
        alreadySeen = []
        for char in self.mystring:
            for i in alreadySeen:       #in here if it found it earlier it will stop
                if char==i:
                    print('No it is not unique.')
                    return
            alreadySeen.append(char)
        print('Yes it is unique.')

def main():
    firstString = Mystring('ezhiwe')  #which not all characters are uniqie
    firstString.isUnique()

if __name__ == "__main__":
    # execute only if run as a script
    main()
''' But for this way it has to look every char in alreadyseen to determine uniqie
    def isUnique(self):
        alreadySeen = []
        for char in self.mystring:
            if char in alreadySeen:
                print('No it is not.')
                return
            alreadySeen.append(char)
        print('Yes it is.')
'''
