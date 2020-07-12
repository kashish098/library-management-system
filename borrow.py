import sqlite3
from db_interface import DbInterface
from display import display

class Borrow:

    @staticmethod
    def display_borrowers():
        query = 'SELECT * FROM issued'
        borrowers = DbInterface.execute_query(query)
        display(borrowers)
