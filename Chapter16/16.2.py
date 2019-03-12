#16.2
#Word Frequencies: Design a method to find the frequency of occurrences of any given word in a book.
#What if we were running this algorithm multiple times?

def count_words(book,word):
    d = make_dict(book)
    if word in d:
        return d[word]
    else:
        return False

def make_dict(book):
    d = dict()
    for word in book:
        if word in d:
            d[word] +=1
        else:
            d[word] = 1
    return d

def main():
    bookText = "Hello this book contains a lots of ezgi word like hey ezgi how are you where are you from ezgi"
    book = bookText.split(" ")
    print(count_words(book,'ezgi'))


if __name__ == '__main__':
    main()
