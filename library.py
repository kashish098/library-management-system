import sqlite3
from db_interface import DbInterface

class Library:
    DB_NAME = 'librarybooks.db'

    @staticmethod
    def add_book_to_library():
        book_name = input('Enter the book name.')
        author_name = input('Enter the author name.')
        available_copies = 0
        try:
            available_copies = int(input('Enter the number of copies.') )
        except ValueError:
            print('Available copies should be an integer')
            raise
        query = "INSERT INTO books(bookName, author, totalCopies, copiesIssued) VALUES('{}','{}',{}, 0 )".format(book_name,author_name, available_copies) 
        DbInterface.execute_query(query)

    @staticmethod
    def remove_book_from_library():
        book_name = input('Enter the book name:')
        query = 'DELETE FROM books WHERE bookName = "{}"'.format(book_name) 
        DbInterface.execute_query(query)