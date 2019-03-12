#7.5 = Online Book Reader: Design the data structures for an online book reader system.
# Design an online book reader.
class BookReader():
    def __init__(self,books):
        self.books = books
    def read_next_book(self):
        if len(self.books):
            return self.books.pop(0).text
        else:
            return None
class Book():
    def __init__(self,text):
        self.text = text
def main():
    book1 = Book('jack gone ..ashsdjnsnl')
    book2 = Book('happily ever after....')
    myreader = BookReader([book1,book2])
    print(myreader.read_next_book())
    print(myreader.read_next_book())

if __name__ == '__main__':
    main()
