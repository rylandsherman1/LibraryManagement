from sqlalchemy.orm import Session
from .database import SessionLocal
from .models.Book import find_book_by_isbn, find_books_by_title, create_book
from .models.BorrowRecord import get_borrow_records_by_book_id


def main_menu():
    while True:
        print("\nWelcome to the Library Management System!\n")
        print("Please choos an option:")
        print("1. Manage Books")
        print("2. Manage Members")
        print("3. Manage Borrow Records")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            manage_books()
        elif choice == "2":
            manage_members()
        elif choice == "3":
            manage_borrow_records()
        elif choice == "4":
            print("Thank yoiu for using the Library Management System. Goodbye")
            break
        else:
            print("Invalid choice, please choose a number between 1-4.")


def manage_books():
    # Implementation for managing books
    while True:
        print("\nManage Books\n")
        print("1. Add a new book")
        print("2. Delete a new book")
        print("3. View all books")
        print("4. Find a book (by ISBN, title, author)")
        print("5. View All Members who have borrowed a specific book")
        print("6. Return to main menu")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            view_all_books()
        elif choice == "4":
            find_book()
        elif choice == "5":
            view_all_members_who_borrowed_a_specific_book
        elif choice == "6":
            break
        else:
            print("Invalid choice, please choose a number between 1-5.")


def add_book():
    # prompt for book details and add to the database
    print("Adding a new book: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    available_copies = input("Enter number of available copies: ")

    book_data = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available_copies": available_copies,
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
    # prompt for book identifiers and delete it from the database
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
    # display all books from the database
    db = SessionLocal()
    try:
        books = get_all_books(db)
        for book in books:
            print(f"{book.id}: {book.title} by {book.author}")
    finally:
        db.close()


def find_book():
    # prompt user to enter search criteria (ISBN, title, author )
    search_option = input("Search by (1) ID or (2) ISBN: ")
    db = SessionLocal()
    try:
        if search_option == "1":
            book_id = input("Enter book ID: ")
            book = find_book_by_id(db, int(book_id))
        elif search_option == "2":
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
    # prompt user to enter search criteria (ISBN, title, author )
    print("\nView All Members Who Borrowed A Specific Book")

    search_option = input("search by (1) ISBN or (2) Title: ")
    db = SessionLocal()

    try:
        if search_option == "1":
            isbn = input("Enter ISBN: ")
            book = find_book_by_isbn(db, isbn)
        elif search_option == "2":
            title = input("Enter book title: ")
            book = find_books_by_title(db, title)
        else:
            print("Invalid Option.")
            return

        if book:
            borrow_records = get_borrow_records_by_book_id(db, book.id)
            if borrow_records:
                print(f"\nMembers who borrowed '{book.title}':")
                for record in borrow_records:
                    print(
                        f"Member ID: {record.member.id} | Borrow Date: {record.borrow_date}"
                    )
            else:
                print("No borrow recrods found for this book.")
        else:
            print("No book foudn with the given criteria.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close


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

        if choice == "1":
            register_member()
        elif choice == "2":
            delete_member()
        elif choice == "3":
            view_all_members()
        elif choice == "4":
            find_member()
        elif choice == "5":
            find_all_books_borrowed_by_member()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please choose a number between 1-5.")


def register_member():
    # prompt for member details and add to the database
    print("Register Member functionality not yet implemented")


def delete_member():
    # prompt for member identifiers and delete them from the database
    print("Delete Member functionality not yet implemented")


def view_all_members():
    # display all members from the database
    print("View All Members functionality not yet implemented")


def find_member():
    # prompt user to enter search criteria (membership number, name, email )
    print("Find Member functionality not yet implemented")


def find_all_books_borrowed_by_member():
    # prompt user to enter search criteria (membership number, name, email )
    print("Find All Books Borrowed By Member functionality not yet implemented")


def manage_borrow_records():
    # Implementation for managing borrow_records
    while True:
        print("\nManage Borrow Records\n")
        print("1. Create a new borrow record")
        print("2. Delete a borrow record")
        print("3. View all borrow record")
        print("4. View books borrowed by a member")
        print("5. View members who borrowed a book")
        print("6. Return to main menu")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_borrow_record_cli()
        elif choice == "2":
            delete_borrow_record_cli()
        elif choice == "3":
            view_all_borrow_records_cli()
        elif choice == "4":
            view_books_borrowed_by_member_cli()
        elif choice == "5":
            view_members_who_borrowed_book_cli()
        elif choice == "6":
            break
        else:
            print("Invalic choice, please choose a number between 1-6.")


def create_borrow_record():
    book_id = input("Enter book ID: ")
    member_id = input("Enter member ID: ")

    db = SessionLocal()
    try:
        create_borrow_record(
            db,
            {
                "book_id": int(book_id),
                "member_id": int(member_id),
                # "return_date": You can add this if you want to set a return date upon record creation
            },
        )
        print("Borrow record created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()


def delete_borrow_record():
    record_id = input("Enter the borrow record ID to delete: ")

    db = SessionLocal()
    try:
        if delete_borrow_record(db, int(record_id)):
            print("Borrow record deleted successfully.")
        else:
            print("Borrow record not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()


def view_all_borrow_records():
    db = SessionLocal()
    try:
        records = get_all_borrow_records(db)
        for record in records:
            print(
                f"Record ID: {record.id}, Book ID: {record.book_id}, Member ID: {record.member_id}"
            )
    finally:
        db.close()


def view_books_borrowed_by_member():
    member_id = input("Enter member ID: ")

    db = SessionLocal()
    try:
        records = get_borrow_records_by_member_id(db, int(member_id))
        for record in records:
            print(
                f"Book ID: {record.book_id}, Borrow Date: {record.borrow_date}, Return Date: {record.return_date}"
            )
    finally:
        db.close()


def view_members_who_borrowed_book():
    book_id = input("Enter book ID: ")

    db = SessionLocal()
    try:
        records = get_borrow_records_by_book_id(db, int(book_id))
        for record in records:
            print(
                f"Member ID: {record.member_id}, Borrow Date: {record.borrow_date}, Return Date: {record.return_date}"
            )
    finally:
        db.close()


if __name__ == "__main__":
    main_menu()
