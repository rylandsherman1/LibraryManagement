from Book import create_book
from sqlalchemy.orm import Session
from database import SessionLocal



def main_menu():
    while True:
        print("\nWelcome to the Library Management System!\n")
        print("Please choos an option:")
        print("1. Manage Books")
        print("2. Manage Members")
        print("3. Manage Borrow Records")
        print("4. Exit")
        
        choice = input("Enter your choice(1-4): ")
        
        if choice == '1':
            manage_books()
        elif choice == '2':
            manage_members()
        elif choice == '3':
            manage_borrow_records()
        elif choice == '4':
            print("Thank yoiu for using the Library Management System. Goodbye")
            break
        else:
            print("Invalid choice, please choose a number between 1-4.")

def manage_books():
    #Implementation for managing books
    while True:
        print("\nManage Books\n")
        print("1. Add a new book")
        print("2. Delete a new book")
        print("3. View all books")
        print("4. Find a book (by ISBN, title, author)")
        print("5. View All Members who have borrowed a specific book")
        print("6. Return to main menu")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            delete_book()
        elif choice == '3':
            view_all_books()
        elif choice == '4':
            find_book()
        elif choice == '5':
            view_all_members_who_borrowed_a_specific_book
        elif choice == '6':
            break
        else: 
            print("Invalid choice, please choose a number between 1-5.")

def add_book():
    #prompt for book details and add to the database
    print("Adding a new book: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    available_copies = input("Enter number of available copies: ")
    
    book_data = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'available_copies': available_copies,
    }
    
    db = SessionLocal()
    try:
        new_book = create_book(db, book_data)
        print(f"Book added {new_book.title} by {new_book.author}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()
        
def delete_book():
    #prompt for book identifiers and delete it from the database
    book_id = input("Enter the book ID to delete: ")
    db = SessionLocal()
    try:
        if delete_book(db, int(book_id)):
            print("Book deleted from database.")
        else:
            print("Book not found.")
    except ValueError:
        print("Invalid input. Please enter a valid book ID.")
    finally:
        db.close()
    
    
def view_all_books():
    #display all books from the database
    db = SessionLocal()
    try:
        books = get_all_books(db)
        for book in books:
            print(f"{book.id}: {book.title} by {book.author}")
    finally:
        db.close()    
    
def find_book():
    #prompt user to enter search criteria (ISBN, title, author )
    search_option = input("Search by (1) ID or (2) ISBN: ")
    db = SessionLocal()
    try:
        if search_option == '1':
            book_id = input("Enter book ID: ")
            book = find_book_by_id(db, int(book_id))
        elif search_option == '2':
            isbn = input("Enter ISBN: ")
            book = find_book_by_(db, isbn)
        else:
            print("Invalid option.")
            return

        if book:
            print(f"Found Book: {book.title} by {book.author}")
        else:
            print("No book found with the given criteria.")
    except ValueError:
        print("invalid input.")
    finally:
        db.close()
    
    
def view_all_members_who_borrowed_a_specific_book():
    #prompt user to enter search criteria (ISBN, title, author )
    print("View All Members Who Borrowed A Specific Book functionality not yet implemented")
    
def manage_members():
    while True:
        print("\nManage Members\n")
        print("1. Add a new member")
        print("2. Delete a member")
        print("3. View all members")
        print("4. Find a member (by membership number, name, email)")
        print("5. Find All Books Borrowed by Member")
        print("6. Return to main menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            register_member()
        elif choice == '2':
            delete_member()
        elif choice == '3':
            view_all_members()
        elif choice == '4':
            find_member()
        elif choice == '5':
            find_all_books_borrowed_by_member()
        elif choice == '6':
            break
        else: 
            print("Invalid choice, please choose a number between 1-5.")

def register_member():
    #prompt for member details and add to the database
    print("Register Member functionality not yet implemented")
def delete_member():
    #prompt for member identifiers and delete them from the database
    print("Delete Member functionality not yet implemented")
def view_all_members():
    #display all members from the database
    print("View All Members functionality not yet implemented")
def find_member():
    #prompt user to enter search criteria (membership number, name, email )
    print("Find Member functionality not yet implemented")
def find_all_books_borrowed_by_member():
    #prompt user to enter search criteria (membership number, name, email )
    print("Find All Books Borrowed By Member functionality not yet implemented")
        
def manage_borrow_records():
    #Implementation for managing borrow_records
    while True:
        print("\nManage Borrow Records\n")
        print("1. Create a new borrow record")
        print("2. Delete a borrow record")
        print("3. View all borrow record")
        print("4. View books borrowed by a member")
        print("5. View members who borrowed a book")
        print("6. Return to main menu")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            create_borrow_record()
        elif choice == '2':
            delete_borrow_record()
        elif choice == '3':
            view_all_borrow_records()
        elif choice == '4':
            view_books_borrowed_by_member()
        elif choice == '5':
            view_members_who_borrowed_book()
        elif choice == '6':
            break
        else:
            print("Invalic choice, please choose a number between 1-6.")

def create_borrow_record():
    print("create Borrow Record functionality not yet implemented")
def delete_borrow_record():
    print("delete Borrow Record functionality not yet implemented")
def view_all_borrow_records():
    print("View All Borrow Records functionality not yet implemented")
def view_books_borrowed_by_member():
    print("View Books Borrowed by a Member functionality not yet implemented")
def view_members_who_borrowed_book():
    print("View Members Who Borrowed a Book functionality not yet implemented")
    
if __name__ == "__main__":
    main_menu()
    
    
