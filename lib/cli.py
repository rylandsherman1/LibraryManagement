
from Members import create_member as create_member_db
from Members import delete_member as delete_member_db
from Members import get_all_members, find_member_by_id, find_member_by_name, find_member_by_email
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models.Book import find_book_by_isbn, find_books_by_title, create_book
from .models.BorrowRecord import get_borrow_records_by_book_id

from Book import delete_book as delete_book_db
from BorrowRecord import delete_borrow_record as delete_borrow_record_db


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
        if delete_book_db(db, int(book_id)):
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
    print("Register New Member: ")
    name = input("Enter Member's Name: ")
    email = input("Enter Member's Email: ")
    membership_number = input(
        "Enter membership number: "
    )  # should this be automatically generated?

    member_data = {
        "name": name,
        "email": email,
        "membership_number": membership_number,
    }

    db = SessionLocal()
    try:
        new_member = create_member_db(db, member_data)
        print(f"Member added: {new_member.name} with email {new_member.email}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()



def delete_member():
    # prompt for member identifiers and delete them from the database
    member_id = input("Enter the member ID to delete: ")
    db = SessionLocal()
    try:
        if delete_member_db(db, int(member_id)):
            print("Member deleted from database.")
        else:
            print("Member not found.")

    except ValueError:
        print("Invalid input. Please enter a valid member ID.")
    finally:
        db.close()



def view_all_members():
    # display all members from the database
    db = SessionLocal()
    try:
        members = get_all_members(db)
        for member in members:
            print(f"{member.id}: {member.name} - {member.email}")
    finally:
        db.close()

def find_member():
    # prompt user to enter search criteria (membership number, name, email )
    search_option = input("Seach by (1) ID, (2) Name, or (3) Email: ")
    db = SessionLocal()
    try:
        if search_option == "1":
            member_id = input("Enter memver ID: ")
            member = find_member_by_id(db, int(member_id))
        elif search_option == "2":
            name = input("Enter member name: ")
            member = find_member_by_name(db, name)
        elif search_option == "3":
            email = input("Enter member email: ")
            member = find_member_by_email(db, email)
        else:
            print("Invalid option.")
            return

        if member:
            print(f"Found Member: {member.name} with email {member.email}")
        else:
            print("No member found with the given criteria.")
    except ValueError:
        print("Invalid input.")
    finally:
        db.close()



def find_all_books_borrowed_by_member():
    # prompt user to enter search criteria (membership number, name, email )
    member_id = input("Enter the member ID: ")
    db = SessionLocal()
    try:
        borrow_records = get_borrow_records_by_member_id(db, int(member.id))
        if borrow_records:
            print(f"Books borrowed by Member ID {member_id}: ")
            for record in borrow_records:
                book = find_book_by_id(db, record.book_id)
                print(
                    f"Book ID: {book.id}, Title: {book.title}, Borrow Date: {record.borrow_date}"
                )
        else:
            print("No borrow records found for this member.")
    except ValueError:
        print("Invalid input. Please enter a valid member ID.")
    finally:
        db.close()


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
