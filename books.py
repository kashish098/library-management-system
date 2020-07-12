import sqlite3
from db_interface import DbInterface
from display import display
class Books:

    @staticmethod
    def display_all_books():
        query = 'SELECT * FROM books'
        all_books = DbInterface.execute_query(query)
        display(all_books)

    @staticmethod
    def display_available_books():
        query = 'SELECT * FROM books WHERE totalCopies - copiesIssued > 0'
        available_books = DbInterface.execute_query(query)
        display(available_books)    

    @staticmethod
    def display_issued_books():
        query = 'SELECT issued.id, issued.name, books.bookName FROM issued INNER JOIN books WHERE issued.issuedBook = books.bookId'
        issued_books = DbInterface.execute_query(query)
        display(issued_books)

    @staticmethod
    def get_available_book_ids():
        query = 'SELECT bookId FROM books WHERE totalCopies - copiesIssued > 0'
        available_book_ids = DbInterface.execute_query(query)
        book_ids = []
        for book in available_book_ids:
            book_ids.append(book[0])
        return book_ids                        

    @staticmethod
    def get_issued_ids():
        query = 'SELECT id FROM issued'
        issued_ids = DbInterface.execute_query(query)
        issued_book_ids = []
        for issue_id in issued_ids:
            issued_book_ids.append(issue_id[0])
        return issued_book_ids
