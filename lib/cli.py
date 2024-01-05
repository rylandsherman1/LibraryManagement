from .models.Members import create_member as create_member_db
from .models.Members import delete_member as delete_member_db
from .models.Members import (
    get_all_members,
    find_member_by_id,
    find_member_by_name,
    find_member_by_email,
)
from .database import SessionLocal
from .models.Book import (
    find_book_by_isbn,
    find_books_by_title,
    create_book,
    get_all_books,
    find_book_by_id,
    find_books_by_title,
    find_books_by_author,
)
from .models.BorrowRecord import (
    get_borrow_records_by_book_id,
    get_all_borrow_records,
    get_borrow_records_by_member_id,
    BorrowRecord,
    delete_borrow_record as delete_borrow_record_func,  # Renamed import
    create_borrow_record as create_borrow_record_func,  # Renamed import
)

from .models.Book import delete_book as delete_book_db
from .models.BorrowRecord import delete_borrow_record as delete_borrow_record_db

import random


def main_menu():
    while True:
        print("  _      _ _                                                   ")
        print(" | |    (_) |                                                  ")
        print(" | |     _| |__  _ __ __ _ _ __ _   _                          ")
        print(" | |    | | '_ \| '__/ _` | '__| | | |                         ")
        print(" | |____| | |_) | | | (_| | |  | |_| |                         ")
        print(" |______|_|_.__/|_|  \__,_|_|   \__, |                     _   ")
        print(" |  \/  |                        __/ |                    | |  ")
        print(" | \  / | __ _ _ __   __ _  __ _|___/ _ __ ___   ___ _ __ | |_ ")
        print(" | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|")
        print(" | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ ")
        print(" |_|__|_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|")
        print("  / ____|         | |       __/ |                              ")
        print(" | (___  _   _ ___| |_ ___ |___/___                            ")
        print("  \___ \| | | / __| __/ _ \ '_ ` _ \                           ")
        print("  ____) | |_| \__ \ ||  __/ | | | | |                          ")
        print(" |_____/ \__, |___/\__\___|_| |_| |_|                          ")
        print("          __/ |                                                ")
        print("         |___/                                                 ")
        print("\nWelcome to the Library Management System!\n")
        print("Please choose an option:")
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
            print("Thank you for using the Library Management System. Goodbye")
            break
        else:
            print("Invalid choice, please choose a number between 1-4.")


def manage_books():
    # Implementation for managing books
    while True:
        print("  __  __                           ___           _       ")
        print(" |  \/  |__ _ _ _  __ _ __ _ ___  | _ ) ___  ___| |__ ___")
        print(" | |\/| / _` | ' \/ _` / _` / -_) | _ \/ _ \/ _ \ / /(_-<")
        print(" |_|  |_\__,_|_||_\__,_\__, \___| |___/\___/\___/_\_\/__/")
        print("                       |___/                             ")
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
            view_all_members_who_borrowed_a_specific_book()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please choose a number between 1-5.")


def add_book():
    # prompt for book details and add to the database
    print("Adding a new book: ")
    while True:
        title = input("Enter book title: ")
        if len(title) > 0:
            break
        print("Book title cannot be blank. Please enter a valid title.")

    while True:
        author = input("Enter author name: ")
        if len(title) > 0:
            break
        print("Author cannot be blank. Please enter a valid author")

    while True:
        isbn = input("Enter ISBN: ")
        if len(isbn) > 0:
            break
        print("ISBN cannot be blank. Please eneter a valid ISBN.")

    while True:
        available_copies = input("Enter number of available copies: ")
        if available_copies.isdigit() and int(available_copies) >= 0:
            break
        print(
            "Number of available copies must be a non-negative integer. Please enter a valid number"
        )

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
        if books:
            # Print the table headers with specified width for each column
            print(
                "{:<5} {:<50} {:<40} {:<15} {:<10}".format(
                    "ID", "Title", "Author", "ISBN", "Available"
                )
            )
            print("-" * 130)  # Separator line

            for book in books:
                # Format each row of the book data
                print(
                    "{:<5} {:<50} {:<40} {:<15} {:<10}".format(
                        book.id,
                        book.title,
                        book.author,
                        book.isbn,
                        book.available_copies,
                    )
                )
        else:
            print("No books found.")
    finally:
        db.close()


def find_book():
    # prompt user to enter search criteria (ISBN, title, author )
    search_option = input("Search by (1) ID or (2) ISBN or (3) Title or (4) Author: ")
    db = SessionLocal()
    try:
        if search_option == "1":
            book_id = input("Enter book ID: ")
            book = find_book_by_id(db, int(book_id))
            if book:
                print(
                    f"Found Book: {book.title} by {book.author} ISBN: {book.isbn}  Available: {book.available_copies}"
                )
            else:
                print("No book found with the given ID.")
        elif search_option == "2":
            isbn = input("Enter ISBN: ")
            book = find_book_by_isbn(db, isbn)
            if book:
                print(
                    f"Found Book: {book.title} by {book.author} ISBN: {book.isbn}  Available: {book.available_copies}"
                )
            else:
                print("No book found with the given ISBN.")
        elif search_option == "3":
            title = input("Enter Title: ")
            books = find_books_by_title(db, title)
            if books:
                for book in books:
                    print(
                        f"Found Book: {book.title} by {book.author} ISBN: {book.isbn}  Available: {book.available_copies}"
                    )
            else:
                print("No books found with the given title.")
        elif search_option == "4":
            author = input("Enter Author: ")
            books = find_books_by_author(db, author)
            if books:
                for book in books:
                    print(
                        f"Found Book: {book.title} by {book.author} ISBN: {book.isbn}  Available: {book.available_copies}"
                    )
            else:
                print("No books found with the given author.")
        else:
            print("Invalid option.")
            return

    except ValueError:
        print("invalid input.")
    finally:
        db.close()


def view_all_members_who_borrowed_a_specific_book():
    print("\nView All Members Who Borrowed A Specific Book")

    search_option = input("search by (1) ISBN or (2) Title: ")
    db = SessionLocal()

    try:
        if search_option == "1":
            isbn = input("Enter ISBN: ")
            book = find_book_by_isbn(db, isbn)
            if book:
                display_borrow_records_for_book(db, book)
            else:
                print("No book found with the given ISBN.")
        elif search_option == "2":
            title = input("Enter book title: ")
            books = find_books_by_title(db, title)
            if books:
                for book in books:
                    display_borrow_records_for_book(db, book)
            else:
                print("No books found with the given title.")
        else:
            print("Invalid Option.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()


def display_borrow_records_for_book(db, book):
    borrow_records = get_borrow_records_by_book_id(db, book.id)
    if borrow_records:
        print(f"\nMembers who borrowed '{book.title}':")
        for record in borrow_records:
            print(f"Member ID: {record.member.id} | Borrow Date: {record.borrow_date}")
    else:
        print("No borrow records found for this book.")


def manage_members():
    while True:
        print("  __  __                           __  __           _                ")
        print(" |  \/  |__ _ _ _  __ _ __ _ ___  |  \/  |___ _ __ | |__  ___ _ _ ___")
        print(" | |\/| / _` | ' \/ _` / _` / -_) | |\/| / -_) '  \| '_ \/ -_) '_(_-<")
        print(" |_|  |_\__,_|_||_\__,_\__, \___| |_|  |_\___|_|_|_|_.__/\___|_| /__/")
        print("                       |___/                                         ")
        print("\nManage Members\n")
        print("1. Add a new member")
        print("2. Delete a member")
        print("3. View all members")
        print("4. Find a member (by membership ID, name, email)")
        print("5. Find All Books Borrowed by Member")
        print("6. Return to main menu")

        choice = input("Enter your choice (1-6): ")

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
            print("Invalid choice, please choose a number between 1-6.")


def generate_membership_number():
    return random.randint(10000000, 99999999)


def register_member():
    # prompt for member details and add to the database
    print("Register New Member: ")
    while True:
        name = input("Enter Member's Name: ")
        if len(name) > 0:
            break
        print("Name cannot be blank. Please enter a valid name.")

    while True:
        email = input("Enter Member's Email: ")
        if len(email) > 0:
            break
        print("Email cannot be blank. Please enter a valid email.")

    membership_number = generate_membership_number()

    member_data = {
        "name": name,
        "email": email,
        "membership_number": membership_number,
    }

    db = SessionLocal()
    try:
        new_member = create_member_db(db, member_data)
        print(
            f"Member added: {new_member.name} with email {new_member.email} and membership number {new_member.membership_number}"
        )
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
        if members:
            print("{:<5} {:<20} {:<30}".format("ID", "Name", "Email"))
            print("-" * 55)
            for member in members:
                print(
                    "{:<5} {:<20} {:<30}".format(member.id, member.name, member.email)
                )
                # print(f"{member.id}: {member.name} - {member.email}")
        else:
            print("No members found")
    finally:
        db.close()


def find_member():
    # prompt user to enter search criteria (membership number, name, email )
    search_option = input("Seach by (1) ID, (2) Name, or (3) Email: ")
    db = SessionLocal()
    try:
        if search_option == "1":
            member_id = input("Enter ID: ")
            member = find_member_by_id(db, int(member_id))
            if member:
                print(f"Found Member: {member.name} with email {member.email}")
            else:
                print("No member found with the given ID.")

        elif search_option == "2":
            name = input("Enter member name: ")
            members = find_member_by_name(db, name)
            if members:
                print(f"Members found with the name '{name}':")
                for member in members:
                    print(
                        f"- Member ID: {member.id}, Name: {member.name}, Email: {member.email}"
                    )
            else:
                print(f"No members found with the name '{name}'.")

        elif search_option == "3":
            email = input("Enter member email: ")
            member = find_member_by_email(db, email)
            if member:
                print(f"Found Member: {member.name} with email {member.email}")
            else:
                print("No member found with the given email.")

        else:
            print("Invalid option.")
            return

    except ValueError:
        print("Invalid input.")
    finally:
        db.close()


def find_all_books_borrowed_by_member():
    # prompt user to enter search criteria (membership number, name, email )
    member_id = input("Enter the member ID: ")
    db = SessionLocal()
    try:
        borrow_records = get_borrow_records_by_member_id(db, int(member_id))
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
        print("  __  __                           ___                           ___                   _    ")
        print(" |  \/  |__ _ _ _  __ _ __ _ ___  | _ ) ___ _ _ _ _ _____ __ __ | _ \___ __ ___ _ _ __| |___")
        print(" | |\/| / _` | ' \/ _` / _` / -_) | _ \/ _ \ '_| '_/ _ \ V  V / |   / -_) _/ _ \ '_/ _` (_-<")
        print(" |_|  |_\__,_|_||_\__,_\__, \___| |___/\___/_| |_| \___/\_/\_/  |_|_\___\__\___/_| \__,_/__/")
        print("                       |___/                                                                ")
        print("\nManage Borrow Records\n")
        print("1. Create a new borrow record")
        print("2. Delete a borrow record")
        print("3. View all borrow record")
        print("4. View books borrowed by a member")
        print("5. View members who borrowed a book")
        print("6. Return to main menu")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_borrow_record()
        elif choice == "2":
            delete_borrow_record()
        elif choice == "3":
            view_all_borrow_records()
        elif choice == "4":
            view_books_borrowed_by_member()
        elif choice == "5":
            view_members_who_borrowed_book()
        elif choice == "6":
            break
        else:
            print("Invalic choice, please choose a number between 1-6.")


def create_borrow_record():
    book_id = input("Enter book ID: ")
    member_id = input("Enter member ID: ")

    db = SessionLocal()
    try:
        book = find_book_by_id(db, int(book_id))
        if book and book.available_copies > 0:
            borrow_data = {
                "book_id": int(book_id),
                "member_id": int(member_id),
            }
            created_record = create_borrow_record_func(db, borrow_data)

            # Decrease the number of available copies
            book.available_copies -= 1
            db.commit()

            print("Borrow record created successfully.")
            print(
                f"Updated available copies for book ID {book_id}. New count: {book.available_copies}"
            )
        else:
            print("Book is not available for borrowing.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()


def delete_borrow_record():
    record_id = input("Enter the borrow record ID to delete: ")

    db = SessionLocal()
    try:
        # Retrieve the borrow record
        borrow_record = (
            db.query(BorrowRecord).filter(BorrowRecord.id == int(record_id)).first()
        )

        if borrow_record:
            book_id = borrow_record.book_id
            book = find_book_by_id(db, book_id)

            if book:
                # Deleting the borrow record
                if delete_borrow_record_func(
                    db, int(record_id)
                ):  # Using the renamed function
                    print("Borrow record deleted successfully.")

                    # Increase the number of available copies
                    book.available_copies += 1
                    db.commit()
                    print(
                        f"Updated available copies for book ID {book_id}. New count: {book.available_copies}"
                    )
                else:
                    print("Borrow record not found.")
            else:
                print(f"No book found for book ID {book_id}.")
        else:
            print("Borrow record not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()


def view_all_borrow_records():
    db = SessionLocal()
    try:
        records = get_all_borrow_records(db)
        if records:
            # Print table headers
            print(
                "{:<10} {:<30} {:<30} {:<10} {:<10}".format(
                    "Record ID", "Book Title", "Member Name", "Book ID", "Member ID"
                )
            )
            print("-" * 90)  # Separator line

            for record in records:
                # Fetch book and member details
                book = find_book_by_id(db, record.book_id) if record.book_id else None
                member = (
                    find_member_by_id(db, record.member_id)
                    if record.member_id
                    else None
                )

                # Check if any value is None and replace it with a placeholder
                record_id = record.id if record.id is not None else "N/A"
                book_title = book.title if book else "N/A"
                member_name = member.name if member else "N/A"
                book_id = record.book_id if record.book_id is not None else "N/A"
                member_id = record.member_id if record.member_id is not None else "N/A"

                # Format each row of data
                print(
                    "{:<10} {:<30} {:<30} {:<10} {:<10}".format(
                        record_id, book_title, member_name, book_id, member_id
                    )
                )
        else:
            print("No borrow records found.")
    finally:
        db.close()


def view_books_borrowed_by_member():
    member_id = input("Enter member ID: ")

    db = SessionLocal()
    try:
        records = get_borrow_records_by_member_id(db, int(member_id))
        if records:
            # Print table headers
            print(
                "{:<10} {:<15} {:<15}".format("Book ID", "Borrow Date", "Return Date")
            )
            print("-" * 40)  # Separator line

            for record in records:
                # Format each row of data
                book_id = record.book_id if record.book_id is not None else "N/A"
                borrow_date = (
                    record.borrow_date if record.borrow_date is not None else "N/A"
                )
                return_date = (
                    record.return_date if record.return_date is not None else "N/A"
                )

                print("{:<10} {:<15} {:<15}".format(book_id, borrow_date, return_date))
        else:
            print("No records found for this member.")
    finally:
        db.close()


# def view_books_borrowed_by_member():
#     member_id = input("Enter member ID: ")

#     db = SessionLocal()
#     try:
#         records = get_borrow_records_by_member_id(db, int(member_id))
#         for record in records:
#             print(
#                 f"Book ID: {record.book_id}, Borrow Date: {record.borrow_date}, Return Date: {record.return_date}"
#             )
#     finally:
#         db.close()


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
