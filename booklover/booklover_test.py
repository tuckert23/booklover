import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        bl = BookLover("John Smith", "js@virginia.edu", "historical fiction")
        bl.add_book("1984", 3)
        
        self.assertTrue("1984" in bl.book_list.book_name.values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bl = BookLover("John Smith", "js@virginia.edu", "historical fiction")
        bl.add_book("1984", 3)
        bl.add_book("1984", 3)

        self.assertTrue(len(bl.book_list[bl.book_list["book_name"] == "1984"]) == 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        bl = BookLover("John Smith", "js@virginia.edu", "historical fiction")
        bl.add_book("1984", 3)

        self.assertTrue(bl.has_book("1984"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bl = BookLover("John Smith", "js@virginia.edu", "historical fiction")
        bl.add_book("1984", 3)

        self.assertFalse(bl.has_book("The Martian"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        bl = BookLover("John Smith", "js@virginia.edu", "historical fiction")
        bl.add_book("1984", 3)
        bl.add_book("The Martian", 4)
        bl.add_book("The Right Stuff", 2)

        self.assertEqual(bl.num_books_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        bl = BookLover("John Smith", "js@virginia.edu", "historical fiction")
        bl.add_book("1984", 3)
        bl.add_book("The Martian", 4)
        bl.add_book("The Right Stuff", 4)
        fav_books = bl.fav_books()
        self.assertTrue(fav_books.book_rating.where(fav_books.book_rating > 3).all())
                
if __name__ == '__main__':
    unittest.main(verbosity=3)