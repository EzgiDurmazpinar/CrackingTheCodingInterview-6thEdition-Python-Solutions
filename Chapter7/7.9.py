# 7.9 Design an efficient circular array.

class CircularArray():

    def __init__(self, array):
        self.array = array
        self.start = 0

    def rotate(self, i):
        self.start = (self.start + i) % len(self.array)

    def __iter__(self):
        for i in range(self.start, len(self.array)):
            yield self.array[i]
        for i in range(0, self.start):
            yield self.array[i]

    def __getitem__(self, i):
        return self.array[(self.start + i) % len(self.array)]

    def __setitem__(self, i, item):
        self.array[(self.start + i) % len(self.array)] = item

    def __delitem__(self, i):
        index = (self.start + i) % len(self.array)
        del self.array[index]
        if index < self.start:
            self.start -= 1

def main():
    circulararray = CircularArray([1,2,3,4,5])
    circulararray.rotate(2)
    #for item in circulararray:      #__iter__
    #    print(item)
    #del circulararray[2]            #__delitem__
    #for item in circulararray:
    #    print(item)
    #print(circulararray[2])  #__getitem__

    circulararray[2] = 19       #__setitem__
    for item in circulararray:      #__iter__
        print(item)
if __name__ == '__main__':
    main()
