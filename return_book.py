from db_interface import DbInterface
from books import Books

class ReturnBook:

    @staticmethod
    def return_book():
        Books.display_issued_books()
        issue_id = int(input('Enter the issue id of book which you want to return:') )
        issued_ids = Books.get_issued_ids() 

        if issue_id in issued_ids:
            query = 'SELECT issuedBook FROM issued WHERE id = {}'.format(issue_id)
            book_id = DbInterface.execute_query(query)
            book_id = book_id[0][0]

            query = "UPDATE books SET copiesIssued = copiesIssued - 1 WHERE bookId = '{}' ".format(book_id)
            DbInterface.execute_query(query)

            query = "DELETE FROM issued WHERE id = {}".format(issue_id)
            DbInterface.execute_query(query)
            
        else:
            print('Invalid issue id.')