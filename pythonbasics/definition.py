
# Basic class definitions


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title):
        self.title = title


# TODO: create instances of the class
book1 = Book("Swami Vivekanand")
book2 = Book("A Man for All Seasons")

# TODO: print the class and property
print(book1)
print(book1.title)
print(book2.title)
