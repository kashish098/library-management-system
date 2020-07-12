from books import Books
from issue import Issue
from library import Library
from return_book import ReturnBook

print('*********************************************************')
print('Welcome to Library Management System')
print('*********************************************************')

operation = None

while(True):
    print('\nChoose an operation:')
    print('1. Display all the books in library.')
    print('2. Display all the issued books.')
    print('3. Display all the available books.')
    print('4. Issue a book.')
    print('5. Return a book.')
    print('6. Add a book in the library.')
    print('7. Remove a book from the library.')
    print('8. Exit the system.\n')

    try:
        operation = int(input())
    except ValueError:
        print('Operation number must be integer.')

    if operation < 1 or operation > 8:
        print('Enter the valid operation number.')

    elif operation == 1:
        Books.display_all_books()

    elif operation == 2:
        Books.display_issued_books()

    elif operation == 3:
        Books.display_available_books()

    elif operation == 4:
        Issue.issue_book()

    elif operation == 5:
        ReturnBook.return_book()

    elif operation == 6:
        Library.add_book_to_library()

    elif operation == 7:
        Library.remove_book_from_library()

    else:
        print('Thanks for using the library management system.')
        exit()