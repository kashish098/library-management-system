from db_interface import DbInterface
from books import Books

class Issue:
    
    @staticmethod
    def issue_book():
        name = input('Enter your Name:')
        Books.display_available_books()
        try:
            book_id = int(input('Choose the bookId which you want to issue:') )
        except ValueError:
            print('Book Id should be an integer')
            return
        book_ids = Books.get_available_book_ids()

        if book_id in book_ids:
            query = "INSERT INTO issued(name, issuedBook) VALUES('{}',{})".format(name, book_id )
            DbInterface.execute_query(query)

            query = "UPDATE books SET copiesIssued = copiesIssued + 1 WHERE bookId = '{}' ".format(book_id)
            DbInterface.execute_query(query)
        else:
            print('Invalid book Id.')

        

