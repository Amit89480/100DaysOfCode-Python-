# Here we will be solving the program of library management system

class Library:
    def __init__(self):
        self.books = []
        self.noOfBooks = 0

    def addBooks(self, books):
        self.books.append(books)
        self.noOfBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noOfBooks} Books. The books are:: ")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBooks("Web development")
l1.addBooks("Node js")
l1.addBooks("Javascript")
l1.addBooks("TensorFlow")
l1.addBooks("SykitLearn")
l1.showInfo()
