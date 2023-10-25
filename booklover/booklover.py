"""
Book lover class
"""
import pandas as pd

class BookLover():
    """Book lover class
    """

    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, 
                 book_list: pd.DataFrame = pd.DataFrame({"book_name": [], "book_rating": []})) -> None:
        """Constructor for a BookLover object

        Args:
            name (str): name of BookLover
            email (str): email of BookLover
            fav_genre (str): favorite genre of BookLover
            num_books (int, optional): number of books in collection. Defaults to 0.
            book_list (pd.DataFrame, optional): dataframe of book name and rating. Defaults to pd.DataFrame({"book_name": [], "book_rating": []}).
        """
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = book_list
        self.num_books = num_books


    def add_book(self, book_name, rating):
        """
        Adds a book to the collection

        Args:
            book_name (str): name of book to add
            rating (float): rating of book out of five
        """
        new_book = pd.DataFrame({"book_name": [book_name], "book_rating":[rating]})

        if not self.has_book(book_name):
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            print("Book '%s' already exists in book list"%book_name)

    def has_book(self, book_name):
        """Checks collection to see if the book is present

        Args:
            book_name (str): name of book in question

        Returns:
            bool: whether the book is in the collection
        """
        if book_name in self.book_list.book_name.values:
            return True
        else:
            return False

    def num_books_read(self):
        """Gets the number of books in collection

        Returns:
            int: length of book list
        """
        return len(self.book_list)

    def fav_books(self):
        """Returns list of books with a rating greater than 3

        Returns:
            pd.DataFrame: dataframe of books with a rating greater than 3
        """
        return self.book_list[self.book_list["book_rating"]>3]

if __name__ == "__main__":
    test_object = BookLover("Taylor Tucker", "fakeemail@gmail.com", "scifi")
    test_object.add_book("1984", 4)
    test_object.add_book("The Martian", 5)
    test_object.add_book("The Martian", 3)
    test_object.add_book("War of the Worlds", 2)
    print(test_object.num_books_read())
    print(test_object.fav_books())