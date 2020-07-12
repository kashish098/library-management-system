import sqlite3

class DbInterface:

    DB_NAME = 'librarybooks.db'

    @staticmethod
    def connect(db_name = DB_NAME):
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
        except:
            print('Unable to connect to database.')
            raise
        else:
            return conn, cursor

    @staticmethod
    def execute_query(query):
        conn, c = DbInterface.connect()
        res = None
        try:
            c.execute(query)
        except Exception:
            conn.rollback()
            raise
        else:
            conn.commit()
            res = c.fetchall()
        finally:
            conn.close()
            return res        